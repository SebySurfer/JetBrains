import Interface_Ex.Creature;
import Interface_Ex.Demigod;
import Interface_Ex.Human;

import java.awt.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Vector;

public class Main {
    public static void main(String[] args) throws InterruptedException {

//**********************************************************************************************************************
        //Threads

        /*

        * YouTube Notes:
        - Program = line of code that achieves some tasks. The program itself is stored within a Hard-Disk, or your
        local memory (x.java).

        - Process = Once a program is executed, it takes the RAM, or the Main Memory.

        Local Hard-Disk                                 RAM
            x.java          ----- Executing ---->
          "Program"                                    Process


        - Multi-processing = process of being able to execute two or more processes of computational jobs at a time

        - Threads = are used to preform a task within a Process.
        - Multiple threads = allows to preform multiple tasks at the same time, in a Process
        There are (or can have) multiple threads in a single process, and each thread independent of the other
            Real ex = YouTube preforms multiple tasks, such as = playing the video, giving adds, creating related
            videos, creating the comment section, etc. Each one of these is called a thread.

        A process can have multiple threads, but threads have their own local variables and local memory.

        Thread Life-cycle:
        New --> Runnable --> Running --> Waiting --> Dead --> (Repeat)

        1. New = it will not start executing until a process is being assigned to it
        2. Runnable = thread is assigned to a process and engaged
        3. Running = the code is executed
        4. Waiting = still in the running stage, but it needs a response
        5. Dead = process is terminated when received the response, or finishes the task by itself


        * Code Academy:
        Sequential Programs = programs that run instructions in a defined order, with a beginning and an end

        For most applications, the primary requierements are: being fast and efficient
        To meet this goal, we have to implement concurrent programs.

        Concurrent Programs = enables the execution of multiple tasks at the same time

        Threads = they are the building blocks of Concurrent Programs. A single thread has a beginning and an end,
        with only a single point of execution.

        A program can have multiple threads running simultaneously

        By default, a process has a single thread of execution, being the main thread. From the initial thread, we can
        create more threads to launch different independent tasks. The process isn't considered finished until all
        threads have finished.

        PURPOSE:
        Whenever we have a web page or an application without threads, people will confront the problem of having to
        wait for all the tasks to be completed sequentially before being able to preform any other actions on the site.

        Using a multithreaded program, however, it can stack independent actions while still allowing you to do other
        tasks simultaneously. In other words, it allows actions to do things in parallel with one-another.
        It prevents your program’s main thread to become unresponsive or unusable while the tasks are being performed.

        CONTEXT:

        Programs Context = it includes variables, function names, etc.

        Context of threads can run independently, or dependently (between threads as well)

        Problem that arises:
        When reading shared information in a multi-threaded program, there's nothing to worry about when managing
        SHARED STATE. However, when multiple threads are modifying the same source, we can run into issues on changing
        values from threads that have out-of-date variables.

        - Thread Synchronization = it's the solution when facing this problem of managing issues of Shared State.


         */


        /*
        Using threads example:
        We are using a class example with Printer
         */

        Printer smallPrinter = new Printer(2, "You can't see this because its white", false);
        Printer bigPrinter = new Printer(10, "Text", true);

        //bigPrinter.printText();
        //smallPrinter.printText();


        //In this way, the program will run sequentially on the order that you placed the commands


        //However, to prioritize on the ones that execute sooner from less processing time, we use our threads as so:

        //bigPrinter.start();
        //smallPrinter.start();

        //Here you can see clearly that even though the big printer started first, the small printer gained priority
        // for running the least amount of code first



        // ---------

        /*
        Bro Code:

        Each thread can execute parts of your code in parallel with the main thread

        Each thread has a priority.

        Threads with higher priority are executed in preference compared to threads with a lower priority

        The Java cirtual machine continues to execute threads until either one of the following occurs:
            1. The exit method of class Runtime has been called
            2. All user threads have died

            When the Java VM starts up, there is a thread which calls the main method, which is a thread that
            is called "main"


         */

        //System.out.println(Thread.activeCount());

        /*
        If you can see, the active counts has a value of 2. How ?
        It is including the main thread, and the other class thread we made, named "Printer"
        Any objects created within that class isn't a new thread, they're elements within the same thread.
         */

        Thread.currentThread().setName("Main Thread");

        //System.out.println(Thread.currentThread().getName());

        Thread.currentThread().setPriority(9);

        // Priorities are set between the numbers of 1 - 10

        //System.out.println(Thread.currentThread().getPriority());
        //System.out.println(Thread.currentThread().isAlive());

        MyThread thread3 = new MyThread();
        //thread3.start();

        /*
        Whenever we create a new thread, we have to start it. Regarldess if you use the run() method, it's still
        going to be inactive
         */

        //System.out.println(thread3.isAlive());
        thread3.setName("Third Thread");
        //System.out.println(thread3.getName());

        thread3.setPriority(4);

        //System.out.println(thread3.getPriority());

         /*
        You will notice that it has the same priority as the one we set for the main. This is because it inherits
        the priority of the thread that created it
         */


        //System.out.println(Thread.activeCount());

        /*
        2 types of threads:
            1. Normal/User threads (that are already assigned by default)
            2. Daemon threads = low priority thrraad that runs in the background to perform tasks such as garbage
            collection and the JVM terminates itself when all user threads (non-daemon threads) finish their execution
         */

        MyThread thread4 = new MyThread();


        /*
        IMPORTANT NOTE = You cannot set a thread as a daemon after it has already been started.
        Once a thread has been started, you cannot change its daemon status.


         */

        thread4.setDaemon(true);
        //thread4.start();
        //System.out.println(thread4.isDaemon());

        //System.out.println(Thread.activeCount());

        /*
        If you noticed so far, once you let all the print statements to run at the same time, it doesn't quite go
        sequentially. This is where you indirectly applied multi-threading
         */

        //Multi-Threading
        /*
        Concept = process of executing multiple threads simultaneously
        Helps maximum utilization of CPU
        Threads are independent, they don't affect the execution of other threads
        An exception in one thread will not interrupt other threads
        It is useful to serving multiple clients, multiplayer games, or other mutually independent tasks

        Benefits of Multi-Threading:
        If one of the threads encounters an exception and gets interrupted, the other threads will still continue.

         */

        //Method 1 of making a thread
        /*
        Creating a subclass of the Thread class
        Why use this method ?

        It's suitable when you want to create a thread that is tightly coupled with its behavior and do not need
        to extend any other class, as Java doesn't support multiple inheritance.

        It can implement another interface, for ex:
        MyThread extends Thread implements x
         */
        MyThreadCounter thread1 = new MyThreadCounter();

        //Method 2 of making a thread
        /*
        Create a class that implements the runnable interface, and then you take this instance and pass it as an
        argument to the constructor of the thread class, and that's how you get your other thread

         Why do this method ?

         Unlike extending Thread, implementing Runnable allows a class to extend another class while implementing
         the Runnable interface, overcoming Java's single inheritance limitation.

         Inheritance can be allowed through this method by:
         Class 'extends' another_class implements Runnable
         */
        MyRunnable runnable1 = new MyRunnable();
        Thread thread2 = new Thread(runnable1);



        /*
        Now lets take into the test when a thread encounters an exception.
        We added a print statement where a number divided by 0 in MyRunnable class.

        We can even do it to the main thread, and the other threads are still going to run independently


         */

        //System.out.println(1/0);

        /*
        join() Method

        calling thread (x: main) will wait until the specified thread dies and/or for x amount of miliseconds

        thread_waiting_to_die.join(miliseconds_to_wait);

        The JVM will wait for all threads to be finished before exiting the program.

         */

        //thread1.start();

        //thread1.join(3000);

        //thread2.start();


        /*
        Demon Threads

        However, the JVM will NOT wait for the daemon threads to be finished before exiting the program.

        The JVM only needs at least one user thread to start running, but will exit regarldess if there's any daemon
        threads or not



         */


        /*
        Additional Notes:
        Prefer implementing Runnable over extending Thread as it provides better separation of concerns and allows
        for more flexibility in class design.

        Extending Thread: Allows you to create unique threads by subclassing the Thread class directly. Each instance
        of your subclass represents a separate thread of execution. This method doesn't necessarily restrict
        inheritance; you can still inherit from other classes, but it does limit your ability to extend other classes
        because Java doesn't support multiple inheritance. Extending Thread doesn't require
        additional inheritance, but it doesn't restrict inheritance either.

        Implementing Runnable: Allows you to create threads by implementing the Runnable interface. This method
        separates the thread's behavior (defined in the run() method) from the thread itself, which promotes better
        code organization and flexibility. Unlike extending Thread, implementing Runnable doesn't restrict your ability
        to extend other classes because it's just an interface, not a class. Implementing
        Runnable allows for creating threads that can inherit from other classes.

        Let's use an analogy involving building construction to explain the differences between extending Thread and
        implementing Runnable:

        Imagine you're constructing two types of buildings: houses and skyscrapers.

        Extending Thread (House Construction):

        When you extend Thread, it's like building a unique house from scratch. Each house (thread) has its own
        distinctive design and functionality, such as the number of rooms and layout. You don't need any pre-existing
        structure (inheritance) because you're starting fresh with each house.
        However, if you decide to build a house with an attached garage later on, you'll have to demolish and rebuild
        the entire house because Java doesn't support adding additional inheritance to a class that already extends
        Thread. Implementing Runnable (Skyscraper Construction):

        Implementing Runnable is akin to constructing skyscrapers using standardized floor plans. Each skyscraper
        (thread) follows the same basic blueprint (the Runnable interface) but can have different interior designs and
        functions (the run() method implementation). Since you're not tied to a specific building design (class
        inheritance), you can choose to build a residential skyscraper with apartments or a commercial skyscraper with
        office spaces without any restrictions. Additionally, if you decide to add extra features like a rooftop garden
        to all your skyscrapers, you can easily incorporate it into the existing blueprint (implementing interfaces
        doesn't restrict other class inheritance).

        In essence:

        Extending Thread creates unique threads (houses) with their own characteristics but doesn't easily allow for
        additional features or inheritance. Implementing Runnable creates threads (skyscrapers) based on a standard
        blueprint, allowing for consistency and flexibility in design and inheritance.
         */







//**********************************************************************************************************************
        //String Types

        /*
        Strings = it cannot be changed or modified. Every time you need a modification, you need to create or it will
        create a new String object or a String variable. This is the common one that we always use
         */


        /*
        String Buffers = strings that CAN be modified. It's thread-safe and synchronized, allowing you to modify the
        contents of a string without creating a new object every time.
         */

        StringBuffer mybuffer = new StringBuffer("Your name");

        mybuffer.append(", and me");
        //System.out.println(mybuffer);

        /*
        String Builder = strings can ALSO be modified. Faster than StringBuffer and consumes less memory, but NOT
        thread-safe
         */

        /*
        Key Differences between String Builders and String Buffers:

        Thread Safety:

        StringBuffer is synchronized, meaning it is thread-safe. This ensures that multiple threads cannot access it
        simultaneously, which prevents data corruption or inconsistent results in a multithreaded environment.
        StringBuilder is not synchronized, making it faster in single-threaded environments but potentially unsafe
        in multithreaded scenarios.

        Performance:

        StringBuffer is generally slower than StringBuilder due to its synchronized nature. When multiple threads are
        not involved, using StringBuffer can introduce unnecessary overhead.
        StringBuilder is faster in single-threaded scenarios because it lacks the synchronization overhead of
        StringBuffer. It's typically preferred when thread safety is not a concern.

        Mutability and Flexibility:

        Both StringBuffer and StringBuilder are mutable, meaning that the content of the string they hold can be
        modified after it's created.
        StringBuilder offers the same functionality as StringBuffer, but without the synchronization overhead.
        Therefore, it's often the preferred choice unless thread safety is explicitly required.

         */

//**********************************************************************************************************************
        //Interfaces
        /*
        Definition = it's a template that can be applied to a class. Similar to inheritance, but specifies what a clas
        has/must do, it cannot say HOW to do it.
        Classes can apply more than one interface, however, inheritance is limited to 1 super class
        (it cant inherit more than one super class)

        In other words, an interface is simply an outline of what an object should have. Once you start creating
        objects, the interface on itself is a guide to what methods should it implement. Every object will implement
        the methods its own way, but will still retain an orderly fashion.

        The cool thing about it, is that objects can implement more than just one interface.

        3 Key rules:
        1 - Abstract Methods = A class implementing an interface MUST provide implementations (overrides) for all
        abstract methods from the interface, or else it will create errors.
        2 - Default Methods = Interfaces can have default methods with actions provided, but it's needed to include
        "default". This means that the class itself has an option to override the method or just keep the default
        setting
        3 - class may choose to use or not use the methods inherited from the interface based on its requirements.
        It is not required to utilize every method declared in the interface.


        Analogy to differentiate between Objects and Interfaces in Java:

        Analogy: Building Construction

        Class as a Blueprint:

        Imagine a blueprint for constructing a house. This blueprint provides detailed instructions on how the house
        should be built, including the layout, dimensions, materials, and features.
        Similarly, a class in Java acts as a blueprint for creating objects. It defines the structure, behavior, and
        state of objects of that class. Just like how a blueprint guides the construction of a house, a class guides
        the creation and behavior of objects.
        Interface as a Contract:

        Now, consider a contract between a homeowner and a construction company. The contract specifies certain
        requirements and expectations that the construction company must fulfill when building the house. For example,
        it might specify the number of rooms, the quality of materials, and the completion timeline.
        Similarly, an interface in Java acts as a contract between different parts of a program. It specifies a set of
        methods that a class implementing the interface must provide. Just like how a contract defines obligations for
        the construction company, an interface defines obligations for implementing classes.
        Relationship:

        In this analogy, the blueprint (class) provides a detailed plan for constructing a specific type of house,
        while the contract (interface) specifies the requirements that any construction company (class) must meet to
        be considered compliant.
        A construction company (class) can work on multiple projects (implement multiple interfaces) by following
        different contracts (implementing different interfaces) for each project. Similarly, a class can implement
        multiple interfaces to fulfill different contractual obligations.
        Flexibility:

        The blueprint (class) dictates the specifics of how the house should be built, providing less flexibility
        for customization during construction.
        The contract (interface), however, allows for more flexibility because it only specifies the required behavior
        without dictating how it should be implemented. This allows different classes to provide their own
        implementations of the required behavior, promoting adaptability and interchangeability.


         */


        Creature goblin = new Creature();

        Demigod Elius = new Demigod();

        Human Knight = new Human();

        goblin.spread_wings();

        Elius.fireball();

        Knight.shield();


//**********************************************************************************************************************
        //Lambdas

        /*


         */



//**********************************************************************************************************************
        //Collection Framework

        /*

        Provides an architecture to store and manipulate a group of objects

        Analogy:
            Piggy Bank = Collection framework

            Coins = Objects

        The collection framework subdivides into three parts:
        1. Interfaces = (top most position of the hierarchy), holds abstract classes
        2. Classes
        3. Algorithms


        The Java Collections Framework holds 3 kinds of interfaces, and objects to their respective interface:
        1. List:
        - ArrayList
        - LinkedList
        - Vector

        2. Queue:
        - ArrayDeque
            Deque:
            - PriorityQueue

        3. Set:
        - HashSet
        - LinkedHashSet
            SortedSet:
            - TreeSet

         */

//**********************************************************************************************************************
        //Vectors

        /*
        Vectors are exactly the same as ArrayLists and LinkedLists, however, there's a great difference in preformance.

        Main difference between the other object list classes and vectors:
        A Vector is thread-safe and the other lists isn't.
        Operations on an List aren't synchronized, they are not thread-safe.
        To operate multi-threads on a List at the same time results in completely non-deterministic
        behaviour and exceptions.


        Disadvantages of Vectors:
        I's slower in adding a very large number of items in the list (Vector) in one single thread

        Advantages:
        It is thread safe and synchronized, meaning that it can handle multi-Threads
        This thread safety does come with a performance cost.

        Generally, just use ArrayLists = in the relatively rare circumstances that you need to synchronize those
        individual operations across a bunch of different threads, you can just use a synchronized list wrapper
        to take care of that.


         */

        //Single-Thread Environment: Here we showcase an example on the preformance in a

        int size = 1000000;

        ArrayList<Integer> arrayList = new ArrayList<>();

        //currentTimeMills sets for the currrent time of the system in miliseconds

        long start = System.currentTimeMillis();

        for(int i = 0; i < size; i++){
            arrayList.add(i);
        }

        long end = System.currentTimeMillis();

        System.out.println("Time for ArrayList: " + (end - start) + " ms" );


        start = System.currentTimeMillis();

        Vector<Integer> vector= new Vector<>();

        for(int i = 0; i < size; i++){
            vector.add(i);
        }

        end = System.currentTimeMillis();

        System.out.println("Time for Vector: " + (end - start) + " ms" );


        //As you can notice, the Vector takes twice as much time as the ArrayList


        //Multi-Threaded environment

        // First we create two threads to engage at the same time for an ArrayList

        ArrayList<Integer> multiThread_List = new ArrayList<>();
        start = System.currentTimeMillis();



        Thread t1 = new Thread(() -> {
            for(int i = 0; i < size; i++){
                multiThread_List.add(i);
            }
        });

        Thread t2 = new Thread(() -> {
            for(int i = 0; i < size; i++){
                multiThread_List.add(i);
            }
        });

        t1.start();
        t2.start();
        //The join() method makes sure that until both of those threads are completed, we can continue our work bellow

        t1.join();
        t2.join();

        end = System.currentTimeMillis();
        System.out.println("Time for multi-threaded Arraylist: " + (end - start) + "ms");


        // Then we create two threads to engage at the same time for a Vector


        Vector<Integer> multiThread_Vector = new Vector<>();
        start = System.currentTimeMillis();



        Thread ta = new Thread(() -> {
            for(int i = 0; i < size; i++){
                multiThread_Vector.add(i);
            }
        });

        Thread tb = new Thread(() -> {
            for(int i = 0; i < size; i++){
                multiThread_Vector.add(i);
            }
        });

        ta.start();
        tb.start();

        ta.join();
        tb.join();

        end = System.currentTimeMillis();
        System.out.println("Time for multi-threaded Vector: " + (end - start) + "ms");

        /*
        You can see here that the Vector still took a tole on the time.
        However, once we uncover the number of items in each lists, we'll uncover something quite surprising.

        Logically, we'll have 2 million items for every list
         */

        System.out.println("ArrayList ");






































    }
}