version: "3.9"



services:

  calculationscript:

    image: jmeter_generator

    build:

      context: .

      dockerfile: ./Dockerfile

    volumes:

      - ./data:/root/jmeter_generator



    command: tail -F anything
