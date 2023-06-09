echo ""
echo "

 ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
 ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
 ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
 
"
echo ""

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

sleep 1

echo ''

echo 'Start iproxy'

./iproxy 2222:44 > /dev/null 2>&1 &

echo "Mounting"
./sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p 2222 "root@localhost" 'mount -o rw,union,update /'
echo "Mounted!"

echo "patching RaptorActivation.pem"
./sshpass -p 'alpine' scp -rP 2222 -o StrictHostKeyChecking=no ./FactoryActivation.pem root@localhost:/System/Library/PrivateFrameworks/MobileActivation.framework/Support/Certificates/RaptorActivation.pem
echo "Done"




# Kill iproxy
#kill %1 > /dev/null 2>&1

echo 'Done'

echo ''
