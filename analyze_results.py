import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def analyze_experiment(filename="experiment_results_v2.csv"):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found. Run the experiment first!")
        return

    df = pd.read_csv(filename)
    
    # Filter for Blind mode only for psychometric analysis
    blind_df = df[df['Mode'] == 'Blind'].copy()
    
    if blind_df.empty:
        print("No blind mode data found. Please run the experiment in blind 'T' mode.")
        return

    # Create figure
    plt.figure(figsize=(10, 6))
    plt.title("Flicker Fusion Threshold Analysis (U = K/H)", fontsize=14, fontweight='bold')
    plt.xlabel("Frequency H (Hz)", fontsize=12)
    plt.ylabel("Probability of Seeing Flicker P(U)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)

    colors = {0: 'blue', 1: 'red'}
    labels = {0: 'Relaxed (K=0)', 1: 'Math Load (K > 0)'}

    for k_load in [0, 1]:
        subset = blind_df[blind_df['K_Load_Active'] == k_load]
        if subset.empty:
            continue
            
        # Group by frequency and calculate mean "Saw_Flicker"
        grouped = subset.groupby('H_Frequency')['Saw_Flicker'].agg(['mean', 'count']).reset_index()
        
        # Plot raw points
        plt.scatter(grouped['H_Frequency'], grouped['mean'], 
                    color=colors[k_load], label=f"{labels[k_load]} Data", alpha=0.5)
        
        # Simple logistic-like fit or moving average to show trend
        if len(grouped) > 2:
            # Sort for plotting
            grouped = grouped.sort_values('H_Frequency')
            plt.plot(grouped['H_Frequency'], grouped['mean'].rolling(window=2, min_periods=1, center=True).mean(), 
                     color=colors[k_load], linewidth=2, label=f"{labels[k_load]} Trend")

    plt.axhline(0.5, color='gray', linestyle=':', label="50% Threshold (Fusion Point)")
    plt.legend()
    
    output_path = "flicker_analysis.png"
    plt.savefig(output_path)
    print(f"Graph saved to {output_path}")
    plt.show()

if __name__ == "__main__":
    analyze_experiment()
