package client

import (
	"context"
	"golang-cat-microservice/proto"
	"log"
	"os"

	"google.golang.org/grpc"
)

type Client struct {
	connection *grpc.ClientConn
	Client     proto.OwnerClient
}

func NewOwnerClient(ctx context.Context) *Client {
	opts := grpc.WithInsecure()
	cc, err := grpc.Dial("localhost:50051", opts)
	if err != nil {
		log.Fatal(err)
	}

	client := proto.NewOwnerClient(cc)

	return &Client{
		connection: cc,
		Client:     client,
	}
}

func (cc *Client) Close() {
	err := cc.connection.Close()
	if err != nil {
		os.Exit(0)
	}
}
