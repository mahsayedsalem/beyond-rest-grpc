cd golang-cat-microservice
protoc -I=../proto --go_out=plugins=grpc:./proto ../proto/owner.proto 
protoc -I=../proto --go_out=plugins=grpc:./proto ../proto/cat.proto 

cd ..

cd python-dog-microservice
env/bin/python -m grpc_tools.protoc -I../proto --python_out=./server/generated --grpc_python_out=./server/generated ../proto/dog.proto
env/bin/python -m grpc_tools.protoc -I../proto --python_out=./server/generated --grpc_python_out=./server/generated ../proto/owner.proto

cd ..

cd animal-server
env/bin/python -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/cat.proto
env/bin/python -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/dog.proto
env/bin/python -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/catAnalysis.proto

cd ..

cd golang-cat-analysis-microservice
protoc -I=../proto --go_out=plugins=grpc:./proto ../proto/cat.proto
protoc -I=../proto --go_out=plugins=grpc:./proto ../proto/catAnalysis.proto

cd ..