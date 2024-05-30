import java.io.PrintWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.Scanner;
import java.net.*;

public class Client {
    static class ServerMessage
    {
        private String message;

        public synchronized void setMessage(String message)
        {
            this.message = message;
        }

        public synchronized String getMessage()
        {
            return message;
        }
    }
    public static void main(String[] args) throws IOException{
        if(args.length != 1)
        {
            System.err.println("Missing port arg. Correct usage: java Client <port>");
            System.exit(1);
        }

        int  portN = Integer.parseInt(args[0]);
        try {
            Socket socket = new Socket("localhost", portN);
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
            String message;
            ServerMessage serverMessage = new ServerMessage();

            Thread serverListener = new Thread(() -> {
                try
                {
                    while(true)
                    {
                        String msg = in.readLine();
                        if (msg != null)
                        {
                            serverMessage.setMessage(msg);
                            System.out.println(serverMessage.getMessage());
                        }
                    }
                }
                catch(IOException e)
                {
                    System.err.println("Error reading from server: " + e.getMessage());
                }
            });
            serverListener.start();
            while(true)
            {
                message = read.readLine();
                out.println(message);
                if(message.equals("/exit"))
                {
                    break;
                }
            }
        
        }
        catch(UnknownHostException e)
        {
            System.err.println("Unknown host: " + e.getMessage());
        }
        
    }
}
