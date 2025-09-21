from django.shortcuts import render
from datetime import datetime
from .blockchain_simulation import Blockchain, Block
from .wipe_engine import WipeEngine

# Initialize blockchain
wipe_chain = Blockchain()

def dashboard(request):
    return render(request, 'dashboard.html')

def start_wipe(request):
    device_id = request.GET.get('device', 'DEVICE123')
    device_name = f"{device_id} Device"
    wiping_method = "DoD 5220.22-M"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Simulate wipe process
    engine = WipeEngine(device_name, device_id, wiping_method)
    engine.perform_wipe_simulation()

    # Add to blockchain
    wipe_log_data = {
        "log_id": f"log_{device_id.replace('-', '')}",
        "device_id": device_id,
        "wiping_method": wiping_method,
        "status": "Wipe Successful",
        "timestamp": timestamp
    }
    new_block = Block(len(wipe_chain.chain), timestamp, wipe_log_data, wipe_chain.get_latest_block().hash)
    wipe_chain.add_block(new_block)

    context = {
        'device_id': device_id,
        'device_name': device_name,
        'timestamp': timestamp,
        'wipe_status': "Wipe Successful",
        'method': wiping_method,
        'blockchain_hash': new_block.hash,
        'previous_hash': new_block.previous_hash,
        'log_file': engine.log_file,
        'certificate_file': engine.certificate_file
    }
    return render(request, 'certificate.html', context)