use tonic::{transport::Server, Request, Response, Status};
    use proto::owner_server::{Owner, OwnerServer};
    use proto::{NotifyResponse, NotifyRequest};
    mod proto; 

    #[derive(Default)]
    pub struct MyOwner {}

    #[tonic::async_trait]
    impl Owner for MyOwner {
        async fn notify(&self,request:Request<NotifyRequest>)->Result<Response<NotifyResponse>,Status>{
            println!("Owner of {0} {1} is notified", request.get_ref().animal_name, request.get_ref().animal_type);
            Ok(
                Response::new(NotifyResponse{
                 message:format!("Owner of {0} {1} is notified", request.get_ref().animal_name, request.get_ref().animal_type),
            })
        )
        }
    }

    #[tokio::main]
    async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // defining address for our service
        let addr = "[::1]:50051".parse().unwrap();
    // creating a service
        let owner = MyOwner::default();
        println!("Server listening on {}", addr);
    // adding our service to our server.
        Server::builder()
            .add_service(OwnerServer::new(owner))
            .serve(addr)
            .await?;
        Ok(())
    }