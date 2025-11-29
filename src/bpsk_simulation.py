import numpy as np
import matplotlib.pyplot as plt


def generate_bits(num_bits: int) -> np.ndarray:
    """Generate random bits (0/1)."""
    return np.random.randint(0, 2, num_bits)


def bpsk_modulate(bits: np.ndarray) -> np.ndarray:
    """BPSK modulation: 0 -> -1, 1 -> +1"""
    return 2 * bits - 1


def awgn_channel(signal: np.ndarray, snr_db: float) -> np.ndarray:
    """Pass signal through AWGN channel for a given SNR in dB."""
    snr_linear = 10 ** (snr_db / 10)
    signal_power = np.mean(np.abs(signal) ** 2)
    noise_power = signal_power / snr_linear
    noise = np.sqrt(noise_power / 2) * np.random.randn(*signal.shape)
    return signal + noise


def bpsk_demodulate(received: np.ndarray) -> np.ndarray:
    """Demodulate BPSK signal back to bits using threshold at 0."""
    return (received >= 0).astype(int)


def compute_ber(original_bits: np.ndarray, detected_bits: np.ndarray) -> float:
    """Compute Bit Error Rate (BER)."""
    errors = np.sum(original_bits != detected_bits)
    return errors / len(original_bits)


def simulate_bpsk(num_bits: int = 100000, snr_db_values=None):
    if snr_db_values is None:
        snr_db_values = list(range(0, 11, 1))  # 0 to 10 dB

    bits = generate_bits(num_bits)
    tx_signal = bpsk_modulate(bits)

    ber_results = []

    for snr_db in snr_db_values:
        rx_signal = awgn_channel(tx_signal, snr_db)
        detected_bits = bpsk_demodulate(rx_signal)
        ber = compute_ber(bits, detected_bits)
        ber_results.append(ber)
        print(f"SNR = {snr_db:2d} dB -> BER = {ber:.6f}")

    return snr_db_values, ber_results, tx_signal


def plot_ber(snr_db_values, ber_results, save_path: str):
    plt.figure()
    plt.semilogy(snr_db_values, ber_results, marker='o')
    plt.xlabel('SNR (dB)')
    plt.ylabel('Bit Error Rate (BER)')
    plt.title('BPSK over AWGN: BER vs SNR')
    plt.grid(True, which='both')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def plot_constellation(tx_signal: np.ndarray, snr_db: float, save_path: str):
    rx_signal = awgn_channel(tx_signal, snr_db)
    plt.figure()
    plt.scatter(rx_signal.real, np.zeros_like(rx_signal), alpha=0.3)
    plt.xlabel('In-Phase')
    plt.ylabel('Quadrature')
    plt.title(f'BPSK Constellation (SNR = {snr_db} dB)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


if __name__ == "__main__":
    # Simulation parameters
    NUM_BITS = 100000
    SNR_DB_VALUES = list(range(0, 11, 1))

    snr_db_values, ber_results, tx_signal = simulate_bpsk(
        num_bits=NUM_BITS,
        snr_db_values=SNR_DB_VALUES
    )

    # Save plots
    plot_ber(snr_db_values, ber_results, save_path="../results/ber_vs_snr.png")
    plot_constellation(tx_signal, snr_db=5, save_path="../results/constellation_example.png")