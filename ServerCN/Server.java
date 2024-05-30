import java.io.IOException;
import java.io.PrintWriter;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.List;
import java.util.ArrayList;
import java.net.*;


public class Server {
    public static void main(String[] args) throws IOException{
        if(args.length < 1)
        {
            System.err.println("Missing port. Correct usage: java Server <port>");
            System.exit(1);
        }

        int portN = Integer.parseInt(args[0]);
        System.out.println("Server started listening on port " + portN);

        List<PrintWriter> clientWriters = new ArrayList<>();

        try (ServerSocket server = new ServerSocket(portN)) {
            int k = 0;
            while(true)
            {
                Socket client = server.accept();
                k = k + 1;
                System.out.println("C"+ k+"(" + client + ") connected");

                PrintWriter outprint = new PrintWriter(client.getOutputStream(), true);
                clientWriters.add(outprint);
                new ClientHandler(client, k, clientWriters).start();

            }

        }
        catch (IOException e)
        {
            System.out.println("Error establishing connection: " + e.getMessage());
        }

    }

    
}

class ClientHandler extends Thread {
    private Socket client;
    private int clientNo;
    private List<PrintWriter> clientWriters;

    public ClientHandler(Socket client, int clientNo, List<PrintWriter> clientWriters)
    {
        this.client = client;
        this.clientNo = clientNo;
        this.clientWriters = clientWriters;
    }

    public void run()
    {
        try(
            PrintWriter out = new PrintWriter(client.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
        ) {
            String message;
                while((message = in.readLine()) != null)
                {
                    System.out.println("C"+clientNo+"(" + client.toString() + "): " + message);
                    for (PrintWriter writer : clientWriters)
                    {
                        if(writer != out)
                        {
                            writer.println("C" + clientNo + "(ip:" + client.getInetAddress() + " port: " + client.getPort() + ") " + message);
                        }
                    }
                }
        } catch(IOException e)
        {
            System.err.println("Error handling client: " + e.getMessage());

        }
        finally
        {
            try {
                client.close();
            }
            catch(IOException e) {
                System.err.println("Error at closing client socket: " + e.getMessage());
            }
        }
    }
}
