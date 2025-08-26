#### What is an instruction trace?
An instruction trace is a detailed list of instructions that execute for that process. 
#### What common events lead to the creation of a process?
A process is typically created when the OS is provided with a new batch job, a user logs on to the system, the OS creates it to perform a function on behalf of a user program, or it is spawned by an existing process. 
#### For the processing model of figure 3.6, briefly define each state.
Figure 3.6 describes a five state process model. The states are:
New: This is a process which has been created but has not yet been added to the pool of processes on which work can be done upon.
Ready: This is a process which is in the pool of processes that can be worked on, but is not currently being worked on by the CPU.
Blocked: This is a process which is waiting for an event before work on it can continue.
Running: This is a process which the CPU is currently working on.
Exit: This is a process which has been released from the pool of processes which can be worked upon, either because it has completed or because it aborted for some reason.
#### What does it mean to preempt a process?
A process that is being worked on by the CPU can be interrupted by the OS if another process with higher priority becomes ready or has it's event condition met.
#### What is swapping and what is its purpose?
Swapping is when an OS suspends a process from RAM to space on the hard drive when no part of the process is in the ready state. This frees up room for other processes.
#### Why does Figure 3.9b have two blocked states?
Figure 3.9 depicts two blocked states because there are two versions of a blocked process. One where it is simply blocked but still exists in memory, and one where it is blocked and has been suspended to the hard drive.
#### List four characteristics of a suspended process.
Suspended processes possess the following characteristics:
1. Not available for immediate action.
2. May or may not be waiting for an event.
3. It was suspended by an agent, either itself, a parent process, or the OS.
4. It will not leave the suspended state until the agent says so.
#### For what types of entities does the OS maintain tables of information for management purposes?
The OS has tables of information for memory, I/O, files, and processes.
#### List three general categories of information in a process control block.
The three categories of information in a process control block are:
1. Process identification: a unique identifier for the process.
2. Processor state information: contains the contents of the processor registers.
3. Process control information: additional info which the OS requires to manage current active processes and coordinate them with other processes.
#### Why are two modes (user and kernel) needed?
Kernel mode is needed for complete control over the computer in order to perform hardware functions, however this level of control can be dangerous and is not required by application software so it is run in user mode.
#### What are the steps performed by an OS to create a new process?
The steps required to start a new process include:
1. Assigning a new process identifier.
2. Allocating space for the process.
3. Initialize the process control block.
4. Set the appropriate linkages e.g. linking it to the scheduling queue.
5. Create other relevant data structures like perhaps an accounting file.
#### What is the difference between an interrupt and a trap?
An interrupt is caused by some external event stopping a process like the clock, completion of an I/O operation, or a memory fault. A trap results from an error occurring within the process which could be for example caused by an illegal file access attempt.
#### Give three examples of an interrupt.
Three examples of an interrupt are:
1. Clock interrupt: Processes have a maximum allowable time they can be worked on, called a time slice. 
2. I/O interrupt: When an I/O operation completes, the OS moves all processes waiting on it to the ready state.
3. Memory fault: The processor encounters a virtual memory address reference for a word that is not in main memory, and therefor the process must wait for this to be reconciled as the block is brought out of disk memory in main memory.
#### What is the difference between a mode switch and a process switch?
A mode switch changes the CPU's privilege level between user and kernel, while a process switch stops one process and resumes another.
