package server

import (
	"context"
	"fmt"
	c "golang-cat-analysis-microservice/client"
	"golang-cat-analysis-microservice/proto"
	"io"
	"math/rand"
	"time"

	"google.golang.org/grpc/metadata"
)

type Server struct {
	cc proto.CatClient
}

func NewCatAnalysisService(ctx context.Context) *Server {
	cc := c.NewCatClient(ctx)
	return &Server{
		cc: cc.Client,
	}
}

func (s *Server) AnalyzeSound(ctx context.Context, request *proto.AnalysisRequest) (*proto.AnalysisResponse, error) {

	md, _ := metadata.FromIncomingContext(ctx)
	newCtx := metadata.NewOutgoingContext(context.Background(), md)

	go func() {
		s.BackgroundAnalysis(newCtx, request)
	}()

	return &proto.AnalysisResponse{
		Result: fmt.Sprintf("Analyzing %s ...", request.GetCatName()),
	}, nil
}

func (s *Server) BackgroundAnalysis(ctx context.Context, request *proto.AnalysisRequest) {
	streamRequest := &proto.AnalyzeCatSoundRequest{
		CatName: request.GetCatName(),
	}
	stream, err := s.cc.AnalyzeCatSound(ctx, streamRequest)
	if err != nil {
		fmt.Println(err)
	}
	for {
		meaw, err := stream.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println(meaw)
	}

	fmt.Println("Analyzing ... ")
	rand.Seed(time.Now().Unix())

	analysisResults := []string{
		"Smelly Cat",
		"Good Cat",
		"Bad Cat",
		"Hungry Cat",
	}
	catAnalysisResult := rand.Int() % len(analysisResults)
	res := fmt.Sprintf("%s is %s", request.GetCatName(), analysisResults[catAnalysisResult])
	fmt.Println(res)
}
