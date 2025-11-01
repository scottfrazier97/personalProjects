def base64_encode_decode(prompt, password):
    import base64

    prompt_clean = str(prompt).strip()
    sample_string_bytes = prompt_clean.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    super_secret_pw = "password"
    
    if super_secret_pw != password:
        return base64_string, None
    
    else:
        decoded_bytes = base64.b64decode(base64_bytes)
        decoded_string = decoded_bytes.decode("ascii")

        return base64_string, decoded_string

encoded_string, decoded_original = base64_encode_decode("Hello", "password")
print(f"Encoded string: {encoded_string}\nDecoded original: {decoded_original}")
