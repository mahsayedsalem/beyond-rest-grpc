package main

import (
	"context"
	"fmt"
	"golang-cat-microservice/proto"
	"log"
	"net"

	"google.golang.org/grpc"
)

type server struct {
}

func notifyUser(catName string) {
	fmt.Println("Hello client ...")

	opts := grpc.WithInsecure()
	cc, err := grpc.Dial("localhost:50051", opts)
	if err != nil {
		log.Fatal(err)
	}
	defer cc.Close()

	client := proto.NewOwnerClient(cc)
	request := &proto.NotifyRequest{AnimalName: catName, AnimalType: "cat"}

	resp, _ := client.Notify(context.Background(), request)
	fmt.Println(resp.Message)
}

func (*server) CallCat(ctx context.Context, request *proto.CatRequest) (*proto.CatResponse, error) {
	catName := request.CatName
	fmt.Println(catName + " will " + "MEEEWWWWW")
	response := &proto.CatResponse{
		CatMeaw: catName + ": " + "MEEEWWWWW",
	}
	notifyUser(catName)
	return response, nil
}

func main() {
	address := "localhost:50056"
	lis, err := net.Listen("tcp", address)
	if err != nil {
		log.Fatalf("Error %v", err)
	}

	fmt.Println("Cat Server is running")

	s := grpc.NewServer()
	proto.RegisterCatServer(s, &server{})

	s.Serve(lis)
}
