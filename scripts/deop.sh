#!/bin/bash

# Manda como primer parametro el jugador para quitarle op (./deop.sh ToribioGamer)

[ ! $1 ] && echo "Se necesita al menos 1 jugador" && exit 1
docker exec minecraft-server mc-send-to-console deop $1
