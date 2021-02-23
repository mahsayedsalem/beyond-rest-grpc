package main

import (
	"context"
	"fmt"
	"golang-cat-microservice/proto"
	"golang-cat-microservice/server"
	"log"
	"net"

	"google.golang.org/grpc"
)

func main() {
	address := "localhost:50056"
	lis, err := net.Listen("tcp", address)
	if err != nil {
		log.Fatalf("Error %v", err)
	}

	service := server.NewBranchService(context.Background())
	fmt.Println("Cat Server is running")
	s := grpc.NewServer()
	proto.RegisterCatServer(s, service)

	s.Serve(lis)
}
