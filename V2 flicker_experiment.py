import pygame
import random
import time
import csv
import os

# --- Constants & Configuration ---
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS_CAP = 120  # Aim for high FPS to minimize quantization error in flicker
BG_COLOR = (0, 0, 0)
FLICKER_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 255, 0)  # Matrix Green
FONT_SIZE = 28

class FlickerExperiment:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Quantized Observer V2: Blind 2AFC Experiment (U = K/H)")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Consolas", FONT_SIZE)
        self.large_font = pygame.font.SysFont("Consolas", FONT_SIZE * 2)

        # Variables
        self.h_frequency = 30.0  # Entropy/Flicker Rate (Hz)
        self.k_load_active = False
        self.current_math_problem = ""
        self.math_answer = 0
        self.math_input = ""
        
        # V2 State
        self.trial_mode = False  # Blind testing mode
        self.is_blind = False    # Is the frequency hidden right now?
        self.running = True
        self.last_flicker_time = time.time()
        self.flicker_state = True
        self.results = []
        
        self.generate_math_problem()

    def generate_math_problem(self):
        """Variable K: Increases cognitive load."""
        a = random.randint(10, 50)
        b = random.randint(10, 50)
        op = random.choice(['+', '-', '*'])
        if op == '*':
            a = random.randint(2, 12)
            b = random.randint(2, 20)
            
        self.current_math_problem = f"{a} {op} {b} = ?"
        self.math_answer = eval(f"{a} {op} {b}")
        self.math_input = ""

    def start_blind_trial(self):
        """Starts a randomized trial for 2AFC."""
        self.trial_mode = True
        self.is_blind = True
        # Randomize frequency between 20Hz and 80Hz for testing
        self.h_frequency = round(random.uniform(25.0, 75.0), 1)
        print(f"Blind Trial Started: Presenting {self.h_frequency}Hz")

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                # Manual mode controls
                if not self.is_blind:
                    if event.key == pygame.K_UP:
                        self.h_frequency += 1.0
                    if event.key == pygame.K_DOWN:
                        self.h_frequency = max(1.0, self.h_frequency - 1.0)
                    if event.key == pygame.K_t: # T for Trial / Test
                        self.start_blind_trial()

                # Space toggles K-Load in any mode
                if event.key == pygame.K_SPACE:
                    self.k_load_active = not self.k_load_active
                    if self.k_load_active:
                        self.generate_math_problem()

                # V2: 2AFC Responses
                if self.is_blind:
                    if event.key == pygame.K_y:
                        self.log_result(saw_flicker=True)
                        self.start_blind_trial() # Next trial
                    if event.key == pygame.K_n:
                        self.log_result(saw_flicker=False)
                        self.start_blind_trial() # Next trial
                    if event.key == pygame.K_m: # M to exit blind mode
                        self.is_blind = False

                # Enter logs in manual mode
                elif event.key == pygame.K_RETURN:
                    self.log_result(saw_flicker=True) # In manual mode we assume they see it until they don't
                
                # Math Input handling
                if self.k_load_active:
                    if event.key == pygame.K_BACKSPACE:
                        self.math_input = self.math_input[:-1]
                    elif event.unicode.isdigit():
                        self.math_input += event.unicode
                    elif event.key == pygame.K_TAB:
                        self.generate_math_problem()

    def log_result(self, saw_flicker):
        data = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "H_Frequency": self.h_frequency,
            "K_Load_Active": int(self.k_load_active),
            "Saw_Flicker": int(saw_flicker),
            "Mode": "Blind" if self.is_blind else "Manual"
        }
        self.results.append(data)
        print(f"Logged: Mode={data['Mode']}, H={self.h_frequency}Hz, K={self.k_load_active}, Saw={saw_flicker}")

    def save_to_csv(self):
        if not self.results:
            return
        keys = self.results[0].keys()
        filename = "experiment_results_v2.csv"
        file_exists = os.path.isfile(filename)
        
        with open(filename, "a", newline="") as f:
            dict_writer = csv.DictWriter(f, keys)
            if not file_exists:
                dict_writer.writeheader()
            dict_writer.writerows(self.results)
        print(f"Results saved to {filename}")

    def run(self):
        while self.running:
            self.handle_input()
            
            # --- Logic: Flicker Control ---
            period = 1.0 / (2.0 * self.h_frequency)
            if time.time() - self.last_flicker_time > period:
                self.flicker_state = not self.flicker_state
                self.last_flicker_time = time.time()

            # --- Drawing ---
            if self.flicker_state:
                self.screen.fill(FLICKER_COLOR)
            else:
                self.screen.fill(BG_COLOR)

            # HUD Overlay
            hud_bg = pygame.Surface((500, 240))
            hud_bg.set_alpha(210)
            hud_bg.fill((20, 20, 20))
            self.screen.blit(hud_bg, (10, 10))

            # Logic for hiding info in Blind Mode
            if self.is_blind:
                h_display = "H: [HIDDEN]"
                instr_2afc = self.font.render("DO YOU SEE FLICKER? [Y/N]", True, (255, 255, 0))
                self.screen.blit(instr_2afc, (20, 135))
                instr_exit = self.font.render("Press M to return to Manual Mode", True, TEXT_COLOR)
                self.screen.blit(instr_exit, (20, 175))
            else:
                h_display = f"H (Entropy): {self.h_frequency} Hz"
                instr_manual = self.font.render("UP/DOWN: Adjust H | T: Start Blind Trial", True, TEXT_COLOR)
                self.screen.blit(instr_manual, (20, 135))
                instr_log = self.font.render("ENTER: Log | ESC: Exit & Save", True, TEXT_COLOR)
                self.screen.blit(instr_log, (20, 175))

            h_text = self.font.render(h_display, True, TEXT_COLOR)
            k_text = self.font.render(f"K (Cognitive Load): {'ACTIVE' if self.k_load_active else 'OFF'}", True, TEXT_COLOR)
            mode_text = self.font.render(f"MODE: {'2AFC (Blind)' if self.is_blind else 'Manual'}", True, (0, 100, 255))
            
            self.screen.blit(h_text, (20, 20))
            self.screen.blit(k_text, (20, 55))
            self.screen.blit(mode_text, (20, 90))

            # Math Problem Overlay
            if self.k_load_active:
                math_surf = self.large_font.render(self.current_math_problem, True, (255, 0, 0))
                # input_surf = self.large_font.render(f"Ans: {self.math_input}", True, (255, 0, 0))
                
                m_rect = math_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                
                math_bg = pygame.Surface((m_rect.width + 100, 120))
                math_bg.set_alpha(180)
                math_bg.fill((0, 0, 0))
                self.screen.blit(math_bg, (SCREEN_WIDTH//2 - (m_rect.width//2 + 50), SCREEN_HEIGHT//2 - 60))
                
                self.screen.blit(math_surf, m_rect)

            pygame.display.flip()
            self.clock.tick(FPS_CAP)

        self.save_to_csv()
        pygame.quit()

if __name__ == "__main__":
    exp = FlickerExperiment()
    exp.run()

if __name__ == "__main__":
    exp = FlickerExperiment()
    exp.run()
