class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        # Passing a checksum with the string.
        str_lens = [str(len(word)) for i,word in enumerate(strs)]
        # print("|".join(strs) + ";" + "|".join(str_lens) )
        return "|".join(strs) + ";" + "|".join(str_lens) 
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        words = []
        main_s = s.rsplit(";", 1)[0]
        print("1")
        lengths = [int(w_len) for w_len in s.rsplit(";", 1)[1].split("|")]
        
        i = 0
        for length in lengths:
            words.append(main_s[i:i+length])
            i += length + 1
        return words
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))