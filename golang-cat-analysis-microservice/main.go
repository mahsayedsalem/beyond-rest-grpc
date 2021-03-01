package main

import (
	"context"
	"fmt"
	"golang-cat-analysis-microservice/proto"
	"golang-cat-analysis-microservice/server"
	"log"
	"net"

	"google.golang.org/grpc"
)

func main() {
	address := "localhost:50057"
	lis, err := net.Listen("tcp", address)
	if err != nil {
		log.Fatalf("Error %v", err)
	}

	service := server.NewCatAnalysisService(context.Background())
	fmt.Println("Cat Analysis Server is running")
	s := grpc.NewServer()
	proto.RegisterCatAnalysisServer(s, service)

	s.Serve(lis)
}
