import openai

prompt_init = """
Product description: A home milkshake maker
Seed words: fast, healthy, compact.
Product names: HomeShaker, Fit Shaker, QuickShake, Shake Maker

Product description: A pair of shoes that can fit any foot size.
Seed words: adaptable, fit, omni-fit.
Product names: AdaptFit, OmniSecure, Fit-All, AdaptShoes

Product description: {product_description}
Seed words: {seed_words}
Poduct names: """


def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key


class GeneralModel:
    def __init__(self):
        print("Model Intilization--->")
        # set_openai_key(API_KEY)

    def query(self, prompt, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """

        # arguments to send the API
        kwargs = {
            "engine": "text-davinci-002",
            "temperature": 0.8,
            "max_tokens": 60,
            "best_of": 1,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
        }

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]

        r = openai.Completion.create(prompt=prompt, **kwargs)["choices"][0][
            "text"
        ].strip()
        return r

    def model_prediction(self, product_description, seed_words, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)
        output = self.query(
            prompt_init.format(
                product_description=product_description, seed_words=seed_words
            )
        )
        return output
