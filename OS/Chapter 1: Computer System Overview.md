#### 1.1 List and briefly define the four main elements of a computer.
The four main parts of a computer are processor, memory, io devices, and system bus. The processor is the brain of the computer completing mathematical operations. Memory stores data and programs currently in use. IO devices allow the computer to communicate with the external environment. The system bus connects all these components allowing information to travel between them.
#### 1.2 Define the two main categories of processor registers.
The two categories of processor registers are memory address unit (MAR) which specifies the address in memory for the next read or write, and memory buffer register (MBR) which contains the data to be written into memory or data read from memory.
#### 1.3 In general terms, what are the four distinct actions that a machine instruction can specify?
Processor - memory: Data transferred between processor and memory or memory and processor.
Pocessor - I/O: Data transferred to or from a peripheral device between the processor and an I/O module.
Data Processing: The processor performs some arithmetic or logical operation on the data.
Control: Specifies a sequence of events that must be executed. 
#### 1.4 What is an interrupt?
An interrupt is a signal to the processor indicating an event that requires immediate attention. The CPU pauses its current task, runs the appropriate interrupt handler, and then resumes its original task.
#### 1.5 How are multiple interrupts dealt with
There are two approaches to dealing with multiple interrupts. The first is to ignore any new interrupt signals until the current interrupt is complete, handling them sequentially. The second is to have a hierarchy of interrupts where some interrupts take priority over others.
#### 1.6 What characteristic distinguish the various elements of a memory hierarchy?
The closer to the top of the memory hierarchy, the faster the access time and the more expensive the cost of hardware per bit. This results in the top being smaller in capacity. The top should ideally contain the memory which is accessed most frequently.
#### 1.7 What is cache memory?
Cache memory is intended to provide memory access time approaching that of fastest memories available and at the same time support a large memory size. It is below registers on the memory hierarchy and above main memory.
#### 1.8 What is the difference between a multiprocessor and multi core system?
Multiprocessor systems have more than on physical CPU, while multi core systems have a single CPU containing multiple cores.
#### 1.9 What is the distinction between spacial locality and temporal locality?
Spatial locality refers for the tendency for instructions to involve clustered memory locations, for example accessing sequential data locations. Temporal locality refers to the tendency of memory locations which have recently been used to be used again.
#### 1.10 In general, what are the strategies for exploiting spatial locality and temporal locality?
In general, spatial locality is exploited by using larger cache blocks while temporal locality is exploited by keeping recently used instructions in cache memory.

