package server

import (
	"context"
	"fmt"
	c "golang-cat-microservice/client"
	"golang-cat-microservice/proto"
	"time"
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
		return nil, err
	}
	fmt.Println(resp.Message)
	return response, nil
}

func (s *Server) AnalyzeCatSound(request *proto.AnalyzeCatSoundRequest, stream proto.Cat_AnalyzeCatSoundServer) error {

	for i := 0; i < 30; i++ {
		time.Sleep(time.Duration(1) * time.Second)
		res := &proto.AnalyzeCatSoundResponse{
			Result: fmt.Sprintf("%s Meaw #%d", request.GetCatName(), i),
		}
		fmt.Println(fmt.Sprintf("%s: Meaw #%d", request.GetCatName(), i))
		if err := stream.Send(res); err != nil {
			return err
		}
	}
	return nil
}
