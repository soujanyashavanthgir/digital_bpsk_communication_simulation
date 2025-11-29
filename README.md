# Digital BPSK Communication Simulation

This project simulates a simple **Binary Phase Shift Keying (BPSK)** digital communication system over an **AWGN (Additive White Gaussian Noise)** channel using Python.

It is designed as an **Electronics & Communication Engineering** mini-project that you can:
- Upload to GitHub as a portfolio project
- Extend with more modulation schemes (QPSK, 16-QAM, etc.)
- Use in reports or presentations

## 🎯 Features

- Random bit generation
- BPSK modulation (+1 / -1 mapping)
- AWGN channel with configurable SNR
- BPSK demodulation and decision logic
- Bit Error Rate (BER) calculation
- BER vs SNR curve
- Constellation scatter plot (received symbols)

## 📁 Project Structure

```text
digital_bpsk_communication_simulation/
├── src/
│   └── bpsk_simulation.py
├── results/
├── requirements.txt
├── README.md
└── LICENSE
```

## 🧠 Theory (Short)

- **BPSK Mapping:** bit 0 → -1, bit 1 → +1  
- **Channel:** s + n, where n is Gaussian noise  
- **Demodulation:** if received value ≥ 0 → bit 1, else bit 0  
- **BER:** number of bit errors / total bits transmitted  

## 🚀 How to Run

1. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate         # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the simulation:

```bash
python src/bpsk_simulation.py
```

This will:
- Print BER values for different SNR levels
- Save plots in the `results/` folder:
  - `ber_vs_snr.png`
  - `constellation_example.png`

## 📊 Extending the Project

Ideas to extend this project for a stronger portfolio:

- Add **QPSK** or **16-QAM** modulation
- Add **Rayleigh fading channel** model
- Compare **theoretical BER** vs **simulated BER**
- Add a simple **command-line interface** to choose modulation or SNR range
- Turn this into a small **GUI tool** using Tkinter or PyQt

## 👤 Author

Soujanya Shavanthigire  
Electronics & Communication Engineering