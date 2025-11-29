🚀 End-to-End BPSK Digital Communication System Simulation

A complete Binary Phase Shift Keying (BPSK) digital communication chain implemented in Python using NumPy and Matplotlib.
This project simulates bit generation → modulation → AWGN channel → demodulation → BER computation → visualization.

Designed for Electronics & Communication Engineering, Digital Communications, Signal Processing, and Wireless Communication portfolios.

📌 Project Overview

This project implements an end-to-end digital communication system using BPSK modulation. It models a realistic wireless channel using Additive White Gaussian Noise (AWGN) and evaluates receiver performance through Bit Error Rate (BER) analysis.

This simulation demonstrates core concepts required in:

Digital communication systems

Wireless signal processing

IoT and embedded communication modules

Modulation/demodulation techniques

Noise modeling and receiver design

The system is fully modular and can be extended to support QPSK, QAM, Rayleigh fading, or channel coding.

🧠 System Architecture
+----------------+     +-----------------+     +---------------+     +-----------------+     +----------------+
| Random Bitstream | → | BPSK Modulator  | →  | AWGN Channel  | →  | BPSK Demodulator | →  | BER Calculator |
+----------------+     +-----------------+     +---------------+     +-----------------+     +----------------+

✔ Bitstream Generation

Generates random 0/1 bits.

✔ BPSK Modulation

Maps:
0 → -1
1 → +1

✔ AWGN Channel

Adds noise according to selected SNR (0–10 dB).

✔ Demodulation

Threshold detection at 0 (hard decision).

✔ BER Calculation

Compares transmitted vs. received bits.

✨ Key Features

End-to-end digital wireless communication simulation

Realistic AWGN channel modeling

BPSK modulation and demodulation

BER vs SNR curve generation

Constellation visualization

Fully configurable simulation parameters

Clean, modular Python code for reuse

📈 Output Visualizations

The simulation generates:

✔ BER vs SNR Plot

Visualizes system performance under increasing noise levels.

✔ BPSK Constellation Diagram

Shows received symbols with Gaussian noise.

These outputs are saved in the results/ folder.

📦 Project Structure
digital_bpsk_communication_simulation/
│
├── src/
│   └── bpsk_simulation.py
│
├── results/
│   ├── ber_vs_snr.png
│   └── constellation_example.png
│
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt

🛠 Installation
1. Clone the repository
git clone https://github.com/soujanyashavanthgir/digital_bpsk_communication_simulation.git
cd digital_bpsk_communication_simulation

2. Install dependencies
pip install -r requirements.txt

▶️ How to Run
python src/bpsk_simulation.py


This will:

Run BPSK simulation

Print BER values for SNR 0–10 dB

Save plots to the results/ folder

📊 Sample Output (Expected)
SNR =  0 dB -> BER ≈ 0.1580
SNR =  2 dB -> BER ≈ 0.0973
SNR =  4 dB -> BER ≈ 0.0481
SNR =  6 dB -> BER ≈ 0.0204
SNR =  8 dB -> BER ≈ 0.0061
SNR = 10 dB -> BER ≈ 0.0011

🎯 Applications

Wireless communication system design

Digital modulation coursework

Signal processing simulation

IoT / embedded communication analysis

Academic mini-projects

Communication engineering portfolios

🔮 Future Improvements

You can extend this project by adding:

QPSK, 16-QAM, OFDM modulation

Rayleigh/Rician fading channels

Adaptive modulation

Channel coding (Hamming, Convolutional, LDPC)

Soft-decision demodulation

Real-time SDR implementation (GNU Radio, HackRF)

👤 Author

Soujanya Shavanthigire
Electronics & Communication Engineering
GitHub: soujanyashavanthgir

📄 License

MIT License

⭐ Like this project?

Give it a star ⭐ on GitHub — it helps grow your portfolio visibility