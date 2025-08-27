#### Table 3.5 lists typical elements found in a process control block for an unthreaded OS. Of these, which should belong to a thread control block and which should belong to a process controll block for a multithreaded system?

#### List reasons why a mode switch between threads may be cheaper than a mode switch between processes. 
Threads share the same resource pool amongst the process they are a part of so switching between them does not require moving new data into memory. Switching between processes means moving the new process' data into memory, which is going to take time.

#### What are the two seperate and potentially independent characteristics embodied in the concept of process?
The two are ownership and execution maybe

#### Give four general examples of the use of threads in a single-user multiprocessing system.

#### What resources are typically shared by all of the threads of a process?

#### List three advantages of ULTs over KLTs

#### List two disadvantages of ULTs over KLTs
When one of the ULTs makes a blocking call it blocks the whole process because the kernel is unaware of individual user threads. Also ULTs can not be truly parallel since the kernel only dedicates one core per process. 

#### Define jacketing
