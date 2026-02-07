<div align="center">

# 👁️ Quantized Observer: The Flicker Fusion Experiment
### Investigating the Observer Effect through Cognitive Load & Visual Perception

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Experimental-orange)](https://github.com/)
[![Science](https://img.shields.io/badge/Science-Cognitive%20Neuroscience-purple)](https://en.wikipedia.org/wiki/Flicker_fusion_threshold)

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Flicker_fusion_threshold.svg/1200px-Flicker_fusion_threshold.svg.png" width="600" alt="Flicker Fusion Illustration (Placeholder)">
  <br>
  <em>Fig 1: Conceptual representation of the Flicker Fusion Threshold.</em>
</p>

</div>

---

## 📜 Abstract

**Quantized Observer** is a scientific research tool designed to empirically test the relationship between **Cognitive Load ($K$)** and **Visual Perception ($U$)**.

Building on the theoretical framework of the **Universal Equation**:
$$U = \frac{K}{H}$$
Where:
- **$U$ (Observer State/Time Perception)**: The inverse of the flicker fusion threshold.
- **$K$ (Cognitive Load)**: The mental effort required to process information (e.g., solving complex arithmetic).
- **$H$ (Entropy/Frequency)**: The rate of visual information (flicker frequency in Hz).

This experiment aims to demonstrate that as **Cognitive Load ($K$) increases**, the **Critical Flicker Fusion Threshold (CFF)** changes, effectively altering the observer's perception of time and reality.

---

## ✨ Key Features

- **🔬 Precision Frequency Control**  
  Adjust flicker rates with `0.1 Hz` accuracy using high-performance Pygame rendering.

- **🧠 Cognitive Load Generator**  
  Integrated arithmetic engine capable of generating randomized problems (Addition, Subtraction, Multiplication) to induce varying levels of mental effort ($K$).

- **⚖️ Blind 2AFC Testing Protocol**  
  Includes a robust **Two-Alternative Forced Choice (2AFC)** mode for objective data collection, eliminating observer bias.
  - Randomized frequency presentation (20Hz - 80Hz).
  - Blind "Yes/No" response logging.

- **📊 Automatic Data Logging**  
  All trials are automatically logged to `experiment_results_v2.csv` with precise timestamps, frequency data, and load conditions.

- **📈 Built-in Analytics**  
  Includes [analyze_results.py](cci:7://file:///c:/Users/Dell/Documents/QUANTAIZED%20OBSERVER%20%28ORIGNAL%29/analyze_results.py:0:0-0:0) to instantly visualize your results, plotting Psychometric Functions specifically comparing **Relaxed (K=0)** vs. **Loaded (K>0)** states.

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- `pip` package manager

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/quantized-observer.git](https://github.com/yourusername/quantized-observer.git)
cd quantized-observer

### 2. Install Dependencies
Install the required Python libraries using pip:
```bash
pip install pygame pandas matplotlib numpy
```

---

## 🚀 Usage

### Running the Experiment
Launch the main experiment interface:
```bash
python "V2 Flicker_Fusion_Experiment.py"
```

### Running the Analysis
After collecting data, run the analysis script to generate graphs:
```bash
python analyze_results.py
```
*This will generate `flicker_analysis.png` showing your threshold shifts.*

---

## 🎮 Controls

### Manual Mode
| Key | Action |
| :--- | :--- |
| **UP / DOWN** | Increase / Decrease Frequency ($H$) |
| **SPACE** | Toggle **Cognitive Load ($K$)** (Show/Hide Math) |
| **T** | Start a **Blind Trial** (Switches to 2AFC Mode) |
| **ENTER** | Log a "Visible Flicker" event manually |
| **ESC** | Save Data & Exit |

### Blind (2AFC) Mode
| Key | Action |
| :--- | :--- |
| **Y** | **Yes**, I see flicker |
| **N** | **No**, the light is steady |
| **M** | Return to Manual Mode |

### Math Input (When Load Active)
| Key | Action |
| :--- | :--- |
| **0-9** | Type Answer |
| **Backspace** | Delete Digit |
| **Tab** | Generate New Problem |

---

## 📂 File Structure

```text
📦 QUANTAIZED OBSERVER
 ┣ 📜 V2 Flicker_Fusion_Experiment.py  # Main Experiment Script (Pygame)
 ┣ 📜 analyze_results.py               # Data Analysis & Plotting Tool
 ┣ 📜 experiment_results_v2.csv        # (Generated) Data Log File
 ┗ 📜 README.md                        # Documentation
```

---

## 🔬 Scientific Methodology

1.  **Baseline Measurement**: The subject determines their CFF threshold in a relaxed state ($K=0$).
2.  **Load Application**: The subject engages the **Cognitive Load** (Spacebar), solving continuous math problems.
3.  **Threshold Retest**: While maintaining the load ($K > 0$), the subject performs Blind Trials ('T') to find the new CFF.
4.  **Hypothesis**: If $U = K/H$, an increase in $K$ must be offset by a change in perceived $H$ (or the threshold of $H$), predicting a **shift in the CFF** during high cognitive load.

---

## 📄 License

This project is open-source and available under the **MIT License**.

> *“The observer is not separate from the observed.”* — J. Krishnamurti (refined by the Quantized Observer Theory)

## 👨‍🔬 About the Author

**Naveen**  
*Lead Researcher & Theoretical Physicist*  
Founder, **Quantum Radio Framework/The Quantized Observer**  
Theoretical Physics & Cognitive Science  
📍 *Kaithal, Haryana, India*

📧 **Correspondence**: [NAVEEN191997@outlook.com](mailto:NAVEEN191997@outlook.com)  
🆔 **ORCID**: [0009-0004-3244-6928](https://orcid.org/0009-0004-3244-6928)  
📚 **Zenodo DOI**: [10.5281/zenodo.18468980](https://doi.org/10.5281/zenodo.18468980)

























