import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

//For Q1

public class Image{

    public int width,height;
    private volatile int x,y;
    private BufferedImage img,outputimage;

    Image(){
        try{
            // read in an image from a file
            img = ImageIO.read(new File("AdvertisementDEMO.jpg"));

            // store the dimensions locally for convenience
            width = img.getWidth();
            height = img.getHeight();

            // setup the starting coordinate for threads to use (getRGB and setRGB)
            x = y = 0;

            // create an output image
            outputimage = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

        }catch(Exception e){
            System.out.println("ERROR " + e);
            e.printStackTrace();
        }
    }

    //Atomically access the x and y coordinate
    public synchronized int[] getRGBWithCoordinate(){
        try{
            int color = img.getRGB(x,y);
            int[] RGBPackage = {x,y,color};

            x++;
            if(x >= width) {
                y++;
                if(y >= height) return null;
                x = 0;
            }

            return RGBPackage;

        }catch(ArrayIndexOutOfBoundsException e){
            return null;
        }
    }

    public int getRGBValue(int x, int y){
        int pixelRGB;
        try{
            pixelRGB = img.getRGB(x, y);
        }catch(ArrayIndexOutOfBoundsException e){
            return 0;
        }
        return pixelRGB;
    }

    public void setPixelonOutputImage(int[] pixel){
        outputimage.setRGB(pixel[0],pixel[1],pixel[2]);
    }

    public void publishOutput(){
        try {
            File outputfile = new File("outputimage.png");
            ImageIO.write(outputimage, "png", outputfile);
        }catch(IOException e){
            System.out.println("ERROR " + e);
            e.printStackTrace();
        }
    }
}
