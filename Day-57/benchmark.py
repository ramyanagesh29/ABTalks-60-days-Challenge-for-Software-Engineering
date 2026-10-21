import statistics
import time
from spam_model import train_model, predict_message

MESSAGES = [
    "Hey, are we still meeting after class?",
    "Congratulations! Claim your free prize now!",
    "Please send me the notes when you can.",
    "Urgent offer, win cash today, call now!",
] * 25

def main():
    started = time.perf_counter()
    model = train_model()
    training_seconds = time.perf_counter() - started

    for message in MESSAGES[:5]:
        predict_message(model, message)  # warm-up
    elapsed = []
    for message in MESSAGES:
        started = time.perf_counter()
        predict_message(model, message)
        elapsed.append(time.perf_counter() - started)

    average = statistics.mean(elapsed)
    print("Local benchmark — not a concurrent server load test")
    print(f"Messages tested: {len(MESSAGES)}")
    print(f"Model training time: {training_seconds:.6f} seconds")
    print(f"Average prediction latency: {average * 1000:.3f} ms")
    print(f"Median prediction latency: {statistics.median(elapsed) * 1000:.3f} ms")
    print(f"Approximate throughput: {1 / average:.1f} predictions/second")

if __name__ == "__main__":
    main()
