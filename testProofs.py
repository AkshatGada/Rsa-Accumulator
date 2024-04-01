from main import setup, batch_add, batch_prove_membership, batch_prove_membership_with_NIPoE, \
    batch_verify_membership, batch_verify_membership_with_NIPoE, batch_delete_using_membership_proofs
from helpfunctions import hash_to_prime, calculate_product


def test_mining(total_utxo_set_size_for_merkle_tree, total_utxo_set_size_for_accumulator, num_of_inputs_in_tx, num_of_outputs_in_tx, num_of_txs_in_block):

    print("--> initialize and fill up accumulator state")
    n, A0, S = setup()
    if total_utxo_set_size_for_accumulator < num_of_inputs_in_tx * num_of_txs_in_block:
        print("please select larger total_utxo_set_size_for_accumulator.")
        return None
    elements_for_accumulator = create_random_list(total_utxo_set_size_for_accumulator)
    inputs_for_accumulator = elements_for_accumulator[0:(num_of_inputs_in_tx * num_of_txs_in_block)]
    outputs_for_accumulator = create_random_list(num_of_outputs_in_tx * num_of_txs_in_block)
    tik = time.time()
    A_post_batch_add, proof = batch_add(A0, S, elements_for_accumulator, n)
    inputs_nonces_list = [S[x] for x in inputs_for_accumulator]
    tok = time.time()
    acc_batch_add_genesis_timing.append(tok - tik)
    print("<--   Done.", acc_batch_add_genesis_timing[-1])

    print("--> prove membership accumulator")
    times = []
    acc_mem_proofs = []
    for i in range(num_of_txs_in_block):
        tik = time.time()
        inputs_list = []
        for j in range(num_of_inputs_in_tx):
            inputs_list.append(inputs_for_accumulator[num_of_inputs_in_tx * i + j])
        acc_mem_proofs.append(batch_prove_membership(A0, S, inputs_list, n))
        tok = time.time()
        times.append(tok - tik)
    sum_times = sum(times)
    acc_batch_prove_mem_timing.append(sum_times / len(times))  # average
    print("<--   Done. total:", sum_times, "; per tx:", acc_batch_prove_mem_timing[-1])
    print()

    print("--> prove membership accumulator")
    times = []
    acc_mem_proofs = []
    for i in range(num_of_txs_in_block):
     tik = time.time()
    inputs_list = []
    for j in range(num_of_inputs_in_tx):
        inputs_list.append(inputs_for_accumulator[num_of_inputs_in_tx * i + j])
    acc_mem_proof = batch_prove_membership(A0, S, inputs_list, n)
    acc_mem_proofs.append(acc_mem_proof)
    tok = time.time()
    times.append(tok - tik)
    sum_times = sum(times)
    acc_batch_prove_mem_timing.append(sum_times / len(times))  # average
    print("<--   Done. total:", sum_times, "; per tx:", acc_batch_prove_mem_timing[-1])

# Print accumulator membership proofs
    print("Accumulator Membership Proofs:")
    for proof in acc_mem_proofs:
     print(proof)

