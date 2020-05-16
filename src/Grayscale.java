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

    /*
    private int calculateConvolution(int x, int y){

        int c1, c2, c3, c4, c5, c6, c7, c8, c9;

        c1 = img.getRGBValue(x-1,y-1);  //Left Top
        c2 = img.getRGBValue(x,y-1);       //Top
        c3 = img.getRGBValue(x+1,y-1);  //Right Top
        c4 = img.getRGBValue(x-1,y);       //Left
        c5 = img.getRGBValue(x,y);            //Center
        c6 = img.getRGBValue(x+1,y);       //Right
        c7 = img.getRGBValue(x-1,y+1);  //Left Bottom
        c8 = img.getRGBValue(x,y+1);       //Bottom
        c9 = img.getRGBValue(x+1,y+1);  //Right Bottom


        int red = (kernel[0] * ((c1 >> 16) & 0xff)) + (kernel[1] * ((c2 >> 16) & 0xff)) + (kernel[2] * ((c3 >> 16) & 0xff)) +
                (kernel[3] * ((c4 >> 16) & 0xff)) + (kernel[4] * ((c5 >> 16) & 0xff)) + (kernel[5] * ((c6 >> 16) & 0xff)) +
                (kernel[6] * ((c7 >> 16) & 0xff)) + (kernel[7] * ((c8 >> 16) & 0xff)) + (kernel[8] * ((c9 >> 16) & 0xff)) ;

        int green = (kernel[0] * ((c1 >> 8) & 0xff)) + (kernel[1] * ((c2 >> 8) & 0xff)) + (kernel[2] * ((c3 >> 8) & 0xff)) +
                (kernel[3] * ((c4 >> 8) & 0xff)) + (kernel[4] * ((c5 >> 8) & 0xff)) + (kernel[5] * ((c6 >> 8) & 0xff)) +
                (kernel[6] * ((c7 >> 8) & 0xff)) + (kernel[7] * ((c8 >> 8) & 0xff)) + (kernel[8] * ((c9 >> 8) & 0xff)) ;

        int blue = (kernel[0] * (c1 & 0xff)) + (kernel[1] * (c2 & 0xff)) + (kernel[2] * (c3 & 0xff)) +
                (kernel[3] * (c4 & 0xff)) + (kernel[4] * (c5 & 0xff)) + (kernel[5] * (c6 & 0xff)) +
                (kernel[6] * (c7 & 0xff)) + (kernel[7] * (c8 & 0xff)) + (kernel[8] * (c9 & 0xff));

        int rgb = (red << 16 | green << 8 | blue);
        return rgb;
    }
    */
}
