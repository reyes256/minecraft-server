#!/bin/bash

# Manda como primer parametro el jugador para hacerlo op (./op.sh ToribioGamer)

[ ! $1 ] && echo "Se necesita al menos 1 jugador" && exit 1
docker exec minecraft-server mc-send-to-console op $1
