# Uncomment this to pass the first stage
import socket


# Function to receive all the data with buffer size of 1024
def read_complete_message(client_socket):
    buffer_size = 1024  # Set buffer size to 1024
    complete_data = b""  # Start with empty data

    while True:
        partial_data = client_socket.recv(buffer_size)
        complete_data += partial_data

        # Check the size of incoming data to break the loop
        if len(partial_data) < buffer_size:
            break

    return complete_data


# Function to check the incoming request type and the route
def check_method_route(client_socket):
    incoming_data_bytes = read_complete_message(client_socket)
    incoming_data_str = incoming_data_bytes.decode("utf-8")

    data_split = incoming_data_str.split(" ")
    request_method = data_split[0]
    request_address = data_split[1]

    print(f"A {request_method} request received for endpoint {request_address}")

    return request_method, request_address


# Handle route responses for task "Extract URL Path"
def handle_route_response(request_address):
    response_proto = "HTTP/1.1"
    response_status = "200"
    response_status_text = "OK"
    content_type = "text/plain"
    content_length = 0
    actual_content = ""

    # Check if the requested route is other than / OR /echo/{str}
    if request_address.startswith("/echo/"):
        actual_content = request_address.split("/")[2]
        content_length = len(actual_content)
    elif request_address != "/":
        response_status = "404"
        response_status_text = "Not Found"

    response_message_str = f"{response_proto} {response_status} {response_status_text}\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n\r\n{actual_content}"

    response_message_bytes = bytes(response_message_str, "utf-8")

    return response_message_bytes


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        client_socket, return_addr = server_socket.accept()  # wait for client
        print(f"The return address is {return_addr}")

        # Read the incoming request and generate response
        _, request_address = check_method_route(client_socket)
        defined_response = handle_route_response(request_address)
        client_socket.sendall(defined_response)
        server_socket.close()


if __name__ == "__main__":
    main()
