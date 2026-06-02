# Quantum basic

### What is quantum computing ?

The main difference between quantum computing and classic computing is their bits, where classic uses bits, quantum computing uses **qubits**.

### What is a **qubits**:
- can act like a classic bit and store either 0 or 1, but also a combination of the both at the same time, this combination or state is called *superposition*.

To vulgarize, lets do a simple example, imagine we got a spinning coin on a table, here we cannot know if it's gonna be heads or tails, this state in quantum computing is called *superposition*, which consists of a mathematical blend of 0 and 1 simulteanously, or heads and tails here, but once it stopped spinning, it returns either 0 or 1.

Now you may ask yourself, but if it returns 0 or 1 like a classic qubits, what is the advantage of using it, and this is where it gets interesting:

Lets say we got a key chain, holding a 1,000,000 key, a classical computer would try each key one by one until it finds the right one, it can take just one try, or a million.

Lets take the same keychain, in quantum computing, we would need exactly one try to find the solution (impressive right?!), but how?
to represent a million we need 20 bits (2^20 = 1,048,576), here it's the same for quantum computing, the process for this example would be:

- We initiliaze all our qubits to 0, here it behave like a classic computer.
- Then we use something called the Hadamard gate (This is where the magic happen).

### Hadamard gate
This Hadamard gate allow all our qubits in a single quantum physical operation, to start spinning (like our coin example), perfectly in a 50/50 superposition state of 0 and 1, and if every single of our qubits is technically 0 and 1, our 20-qubits chain, actually represents now simulteanously every possible 20-bit binary combination that exists (from 0 to 1,048,576) at **the same time**.

```
Classical Register (1 CPU Cycle) = Holds ONE number (e.g., Key #42)
Quantum Register   (1 CPU Cycle) = Holds [000...000] AND [000...001] AND [000...010] ... up to [111...111]
```

Now that we got our 1,000,,000 key representation at the same time, how do we find it?

### Oracle

An oracle acts as a blackbox, you feed it your hadamard gate and will find the correct answer, but how?
 
here is a schema of how it behave:

```
[All Guesses] ---> [ ORACLE CIRCUIT (Logic Gates) ]
                       |
                       +---> Wrong Guess -> Outputs 0 -> Waves pass through untouched
                       |
                       +---> Right Guess -> Outputs 1 -> Interacts with helper qubit -> Wave flips upside down (-)
```

For the sanity of your brain, let's now switch to a different example:
imagine a piano, and we want to detect, which combination of key forms a middle C, our **Hadamard gate** here being, us pressing the 88 key at the same time.

Now let's imagine we send that giant 88-key chord as a single sound-wave towards a wall, we just need to shape a hole in the wall at the exact shape of the middle C sound-wave to identify it right ? The entire wave at once will interact with the wall, but only that middle C through all this combination will actually end up passing through so in a single play of our giant 88-key chord we would be capable of identifying the middle C and the rest will just bounce off the wall.

Well here our "magical wall that identify the middle C" is our **oracle**, and we shape it using wires and gates, shaped the way we want it to be in order to detect our middle C. Once it detects it, the oracle only flags it as this one is the one, by flipping it off negatively, leaving all the other untouched. but how do we find the exact key combination that formed a middle C?

### The diffusion operator & Read()

Well our wave is a series of qubits, as for our piano example, lets say each key is entitled with it's wave, because it's really the case, we know the wave that passes through, so we just need to observe each qubits of that wave, to identify its binary representation.

To do it we firstly need the **diffusion operator** that will allow us to cancel out each key to silence, so the correct key becomes a skyscraper of probability, like turning up the volume for the exact key combination that gave us that middle C. and then we measure, stopping the spin to freeze the qubits at their exact binary sequence of the winning key!

And that is how in quantum computing, we would find which key opens a door out of a million key on our keychain, at once in a single try (This is technically false bc we need to repeat the **oracle + diffusion operator** steps about a 1,000 times to get the volume to 100%)!

To calculate the amount of time we need to repeat can be calculated with:

```
+-------------------+----------------------------+------------------------------+----------------+
| Total Keys (N)    | Classical Avg Tries (O(N)) | Quantum Loops (O(sqrt(N)))   | Speedup Factor |
+-------------------+----------------------------+------------------------------+----------------+
| 100               | 50                         | 7                            | ~7x faster     |
| 1,000,000         | 500,000                    | 785                          | ~630x faster   |
| 1,000,000,000     | 500,000,000                | 24,674                       | ~20,000x faster|
+-------------------+----------------------------+------------------------------+----------------+
```
