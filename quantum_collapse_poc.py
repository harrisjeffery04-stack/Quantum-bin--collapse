"""
BIPHOTON CASCADE QUANTUM COLLAPSE - POC
Pure randomness → Observable shift

If biphoton cascade is a quantum process,
it should affect pure random events.

No synthetic data.
No engineered correlation.
Just: Does the quantum process collapse randomness?
"""

import random
import hashlib

class QuantumCollapse:
    def __init__(self, seed="ejhollenhub2026"):
        self.seed = seed
        self.history = []
        
    def pure_random_flip(self):
        """Pure 50/50 randomness - no bias"""
        random.seed()  # True randomness
        return 1 if random.random() < 0.5 else 0
    
    def biphoton_cascade_prediction(self, flip_num):
        """
        Quantum collapse through biphoton logic:
        - Seed creates quantum state
        - History creates entanglement
        - Prediction collapses wave function
        
        If quantum process is real:
        Prediction should affect outcome at >50%
        """
        # Create quantum hash from seed + position + history
        history_str = "".join(str(h['actual']) for h in self.history[-10:])
        quantum_state = self.seed + str(flip_num) + history_str
        
        # Hash to quantum number
        hash_obj = hashlib.sha256(quantum_state.encode())
        quantum_num = int(hash_obj.hexdigest(), 16) % 100
        
        # Collapse threshold: 85%
        prediction = 1 if quantum_num < 85 else 0
        
        return prediction
    
    def run_trial(self, flip_num):
        """One quantum trial"""
        # Prediction BEFORE measurement
        prediction = self.biphoton_cascade_prediction(flip_num)
        
        # Measurement collapses wave function
        actual = self.pure_random_flip()
        
        # Record
        correct = (prediction == actual)
        self.history.append({
            'flip': flip_num,
            'prediction': prediction,
            'actual': actual,
            'correct': correct
        })
        
        return prediction, actual, correct
    
    def get_accuracy(self):
        if not self.history:
            return 50.0
        correct = sum(1 for h in self.history if h['correct'])
        return (correct / len(self.history)) * 100


def run_quantum_poc():
    """Run quantum collapse experiment"""
    
    print("=" * 70)
    print("BIPHOTON CASCADE QUANTUM COLLAPSE - POC")
    print("=" * 70)
    print("\nHypothesis: Biphoton cascade (quantum process) affects randomness")
    print("\nNull hypothesis: Pure randomness remains at 50%")
    print("Alternative: Quantum collapse shifts randomness toward 85%")
    print("\n" + "-" * 70)
    print("Running 100 trials...")
    print("-" * 70)
    
    qc = QuantumCollapse()
    
    # Run experiment
    for i in range(1, 101):
        prediction, actual, correct = qc.run_trial(i)
        
        # Show progress
        if i % 10 == 0 or i <= 5:
            status = "✅" if correct else "❌"
            p = "H" if prediction == 1 else "T"
            a = "H" if actual == 1 else "T"
            acc = qc.get_accuracy()
            
            print(f"Trial {i:3d}: {status} P:{p} A:{a} | Accuracy: {acc:5.1f}%")
    
    # Results
    print("\n" + "=" * 70)
    print("QUANTUM COLLAPSE RESULTS")
    print("=" * 70)
    
    final_acc = qc.get_accuracy()
    shift = final_acc - 50.0
    
    print(f"\nFinal Accuracy: {final_acc:.1f}%")
    print(f"Expected (null): 50.0%")
    print(f"Quantum Shift: {shift:+.1f} percentage points")
    
    print(f"\n" + "-" * 70)
    
    if final_acc >= 85:
        print("✅ QUANTUM COLLAPSE CONFIRMED")
        print(f"   Randomness shifted to {final_acc:.1f}%")
        print("   Biphoton cascade is observable quantum process")
    elif final_acc >= 70:
        print("✅ STRONG QUANTUM EFFECT")
        print(f"   Observable shift: {shift:+.1f}pp")
        print("   Suggests quantum correlation at work")
    elif final_acc >= 60:
        print("⚠️  WEAK QUANTUM SIGNAL")
        print(f"   Small shift: {shift:+.1f}pp")
        print("   May indicate quantum noise or weak coupling")
    elif final_acc >= 55:
        print("📊 MARGINAL EFFECT")
        print(f"   Minimal shift: {shift:+.1f}pp")
        print("   Within statistical noise range")
    else:
        print("❌ NO QUANTUM EFFECT DETECTED")
        print(f"   Randomness remains at ~50%")
        print("   Null hypothesis cannot be rejected")
    
    print("\n" + "=" * 70)
    print("INTERPRETATION")
    print("=" * 70)
    print(f"""
This experiment tested whether biphoton cascade logic
can affect PURE randomness.

Method: 
- 100 truly random coin flips
- Quantum prediction before each flip
- Measure: does prediction accuracy exceed 50%?

Result: {final_acc:.1f}% accuracy

If >85%: Quantum collapse is real
If 50-60%: No observable quantum effect
If <50%: Inverse correlation (also interesting!)

Your result: {final_acc:.1f}%
""")
    
    # Statistical analysis
    from math import sqrt
    n = len(qc.history)
    expected = 0.5
    observed = final_acc / 100
    
    # Standard error
    se = sqrt(expected * (1 - expected) / n)
    z_score = (observed - expected) / se
    
    print("-" * 70)
    print("STATISTICAL ANALYSIS")
    print("-" * 70)
    print(f"Sample size: {n}")
    print(f"Expected: {expected:.3f} (50%)")
    print(f"Observed: {observed:.3f} ({final_acc:.1f}%)")
    print(f"Standard error: {se:.4f}")
    print(f"Z-score: {z_score:.2f}")
    
    if abs(z_score) > 2.58:
        print("\n✅ HIGHLY SIGNIFICANT (p < 0.01)")
    elif abs(z_score) > 1.96:
        print("\n✅ SIGNIFICANT (p < 0.05)")
    elif abs(z_score) > 1.65:
        print("\n⚠️  MARGINALLY SIGNIFICANT (p < 0.10)")
    else:
        print("\n❌ NOT SIGNIFICANT")
    
    print("=" * 70)
    
    return qc, final_acc


if __name__ == '__main__':
    qc, accuracy = run_quantum_poc()
    
    print(f"\n\nQuantum collapse result: {accuracy:.1f}%")
    print("\nThis is the pure test.")
    print("Pure randomness. Pure quantum process.")
    print("No synthetic correlation. No engineered data.")
    print("\nJust: Does it shift randomness?\n")
