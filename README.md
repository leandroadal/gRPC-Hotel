# gRPC-Hotel

## Descrição

Reserva de Hotel

- O `client.py` faz a requisição de reserva ao servidor ao fornecer a data de check-in e check-out, além do tipo de quarto desejado (solteiro, casal, família) e a categoria (padrão, executivo, luxo).
  
- Em seguida, o servidor fornece informações sobre a disponibilidade (verdadeira ou falsa), o custo por noite e o valor total da estadia, em que a classe `reservation.py` define as propriedades da reserva e a `reservation_service.py` estabelece as regras de negócio.

- As classes `ReservationService_pb2` e `ReservationService_pb2_grpc` foram geradas pelo gRPC com base no arquivo `ReservationService.proto`.
  
## Instalar dependências

- `pip install grpcio grpcio-tools`

## Como executar

- 1 - Iniciar o servidor executando `server.py` que ficara ouvindo na porta 50051.

- 2 - Iniciar o cliente executando `client.py` que enviara ao servidor requisições.
