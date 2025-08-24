#### What are the three objectives of an OS design?
The three objectives of an OS design are:
Convenience: an OS should make a computer easier to use. The OS masks the hardware layer from the programmer, making it easier to interface with the system.
Efficiency: an OS should allow system resources to be used in an efficient manner. An OS must make many decisions like when an I/O device can be used by a program or how much resources to grant to a program. Obviously this all should be done as efficiently as possible. Techniques must be employed to resolve and synchronize claims to resources.
Ability to evolve: an OS should be constructed in such a way so as not to interfere with existing systems when an update is implemented. An OS will evolve over time due to new hardware, new services, or fixes to problems in the OS.
#### What is the kernel of an OS?
The kernel is the heart of the OS, which contains the most frequently used functions in the OS. It has complete control over everything in the system.
#### What is multiprogramming?
Multiprogramming is the concept of holding multiple programs in memory and switching between them when they are waiting for I/O. The benefit of multiprogramming is it allows the cpu to jump to other tasks instead of waiting around, increasing overall efficiency.
#### What is a process?
A process is an executable program as well as the associated data and the execution context needed by the program.
#### How is the execution context of a process used by the OS?
The execution context is the data with which the OS is able to supervise and control the process. It contains crucial information like the program counter, register values, and memory allocation. The OS uses this data for scheduling, resource allocation, and enforcing security policies. 
#### List and briefly explain five storage management responsibilities of a typical OS.
Process isolation: The OS should prevent independent processes from interfering with each other's memory.
Automatic allocation and management: Programs should be allocated across the memory hierarchy automatically.
Support of modular programming: Programmers should be able to create, alter, destroy, and change the size of program modules (units of code).
Protection and access control: At times it is desirable for multiple programs to read the same memory address, however doing so must be done in a way that does not destabilize the programs or the OS.
Long term storage: The OS provides a way for programs to store data for long periods of time, after the computer has been shut down.
#### Explain the distinction between a real address and a virtual address.
A paging system divides a process into a number of fixed sized blocks called pages. A virtual address consists of a page number and an offset within the page. A real address is the physical address in main memory. 
#### Describe the round-robin scheduling technique.
Round robin is a technique where the scheduler gives each process in queue its own turn to run for some time.
#### Explain the difference between a monolithic kernel and a microkernel.
A monolithic kernel provides most of what is thought of as an OS all within the kernel. The kernel is typically then implemented as a single process, with all elements sharing the same address space. A microkernel strips down the kernel to contain only the bare necessities, and outsources the rest to servers aka processes. The two approaches have different theoretical benefits. Linux is a monolith while MacOS employs a hybrid.
#### What is multithreading?
Multithreading is a technique in which a process is divided into threads that can run in parallel.
#### List the key design issues for an SMP operating system.
Symmetric multiprocessing employs multiple processors to do work in parallel, with each processor being able to perform the same functions.
