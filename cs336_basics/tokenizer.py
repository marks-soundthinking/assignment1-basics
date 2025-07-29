# TODO - Learn about tokenizers and upgrade this 
class SimpleBPETokenizer:
    def __init__(self, vocab, merges, special_tokens=None):
        self.vocab = vocab
        self.merges = merges
        self.special_tokens = special_tokens or []

    def encode(self, text):
        # Dummy: just return list of token ids for each byte in text if present in vocab
        return [k for k, v in self.vocab.items() if v in text.encode()]

    def decode(self, token_ids):
        # Dummy: just join bytes from vocab
        return b"".join([self.vocab[i] for i in token_ids if i in self.vocab]).decode(errors="ignore")