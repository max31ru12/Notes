  rabbit:
    image: rabbitmq:3.12.10-management-alpine
    environment:
      - RABBITMQ_DEFAULT_USER=guest
      - RABBITMQ_DEFAULT_PASS=guest
    ports:
      - "15672:15672"
    volumes:
      - ./rabbit:/var/lib/rabbitmq