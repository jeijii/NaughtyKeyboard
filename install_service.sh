#!/usr/bin/env bash

#create service for startup
if [ ! -f /etc/systemd/system/NaughtyKeyboard.service ]; then
           echo "Injecting startup script..."
        cat <<- EOF | sudo tee /etc/systemd/system/NaughtyKeyboard.service > /dev/null
                [Unit]
                Description= Startup Service
                #After=systemd-modules-load.service
                After=local-fs.target
                DefaultDependencies=no
                Before=sysinit.target
                [Service]
                #Type=oneshot
                Type=forking
                RemainAfterExit=yes
                ExecStart=/bin/bash $wdir/boot/boot_script.sh
                StandardOutput=journal+console
                StandardError=journal+console
                [Install]
                WantedBy=multi-user.target
                #WantedBy=sysinit.target
EOF
fi

sudo systemctl enable NaughtyKeyboard.service
