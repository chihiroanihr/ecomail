import py4j.GatewayServer;

public class ImageToGrayscale {
    // Number of threads to use
    public static int threads = 4;
    public static Grayscale[] threadList;
    public volatile int x = 0;
    public static Image img;
    public static GatewayServer gatewayServer;

    public void runImageProcessing(String name){
        try {
            img = new Image(name);
            //create a thread list
            threadList = new Grayscale[threads];

            //start timing
            long startTime = System.currentTimeMillis();

            //start "threads" number of threads
            for(int i = 0; i < threads; i++){
                Grayscale x = new Grayscale(img);
                threadList[i] = x;
            }

            //wait for other threads to complete
            for(int i = 0; i < threads; i++){
                threadList[i].t.join();
            }

            //stop time watch and print out the result
            long endTime = System.currentTimeMillis();

            System.out.println("With " + threads + " thread[s], it took " + (endTime - startTime) + " ms");

            //publish the image we configured
            img.publishOutput();

        } catch (Exception e) {
            System.out.println("ERROR " +e);
            e.printStackTrace();
        }
        //gatewayServer.shutdown();
    }

    public static void main(String[] args) {
        gatewayServer = new GatewayServer(new ImageToGrayscale());
        gatewayServer.start();
    }
}
