package server

import (
	"context"
	"fmt"
	c "golang-cat-microservice/client"
	"golang-cat-microservice/proto"
)

type Server struct {
	oc proto.OwnerClient
}

func NewCatService(ctx context.Context) *Server {
	oc := c.NewOwnerClient(ctx)
	return &Server{
		oc: oc.Client,
	}
}

func (s *Server) CallCat(ctx context.Context, request *proto.CatRequest) (*proto.CatResponse, error) {
	catName := request.CatName
	fmt.Println(catName + " will " + "MEEEWWWWW")
	response := &proto.CatResponse{
		CatMeaw: catName + ": " + "MEEEWWWWW",
	}

	req := &proto.NotifyRequest{AnimalName: catName, AnimalType: "cat"}

	resp, err := s.oc.Notify(ctx, req)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(resp.Message)
	return response, nil
}
