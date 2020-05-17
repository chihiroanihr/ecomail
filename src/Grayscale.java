import java.awt.*;

public class Grayscale implements Runnable {

    Thread t;
    Image img;
    int[] pixel;

    Grayscale(Image target){
        img = target;
        t = new Thread(this);
        t.start();
    }

    public void run(){
        try{
            while(true) {
                //get the coordinate with RGB value atomically
                pixel = img.getRGBWithCoordinate();

                //done!
                if (pixel == null) break;

                //change the RGB value
                Color c = new Color(img.getRGBValue(pixel[0],pixel[1]));
                int red = c.getRed();
                int green = c.getGreen();
                int blue = c.getBlue();

                //To Grayscale
                int average = (red+blue+green)/3;
                red = blue = green = average;

                c = new Color(average, average, average);
                pixel[2] = c.getRGB();

                //set the new RGB value
                img.setPixelonOutputImage(pixel);

                //sleep?
                Thread.sleep(0);
            }
        }
        catch(InterruptedException e){
            System.out.println("Failed");
        }
    }
}
