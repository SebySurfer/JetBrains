public class MyRunnable implements Runnable{
    @Override
    public void run() {
        for(int i = 0; i < 10; i++){
            System.out.println("Thread #2: "+i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            //Thread exception example
            //System.out.println(1/0);

        }
        System.out.println("Thread #2 is finished");

    }
}