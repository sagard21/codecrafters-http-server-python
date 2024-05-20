# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        soc, return_addr = server_socket.accept()  # wait for client
        print(f"The return address is {return_addr}")
        response_proto = "HTTP/1.1"
        response_status = "200"
        response_status_text = "OK"
        response_message = (
            f"{response_proto} {response_status} {response_status_text}\r\n\r\n"
        )
        soc.send(bytes(response_message, "utf-8"))
        server_socket.close()


if __name__ == "__main__":
    main()
