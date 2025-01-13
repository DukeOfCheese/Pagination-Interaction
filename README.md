# discord.py-interaction-pagination

#### discord.py-interaction-pagination is a Python library to easily create embed paginators which uses interaction instead of ctx.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the library.

```bash
pip install discord.py-pagination (pending)
```

## Usage

### Quickstart
```python
import Paginator

# Create a list of embeds to paginate.
embeds = [discord.Embed(title="First embed"),
          discord.Embed(title="Second embed"),
          discord.Embed(title="Third embed")]

... # Inside a command.
await Paginator.Simple().start(interaction, pages=embeds)
```

### Advanced

##### To use custom buttons, pass in the corresponding argument when you initiate the paginator. **THESE ARE OPTIONAL**

```python
# These arguments override the default ones.

PreviousButton = discord.ui.Button(...)
NextButton = discord.ui.Button(...)
PageCounterStyle = discord.ButtonStyle(...) # Only accepts ButtonStyle instead of Button
InitialPage = 0 # Page to start the paginator on.
timeout = 42069 # Seconds to timeout. Default is 60
ephemeral = true # Defaults to false if not passed in.

await Paginator.Simple(
    PreviousButton=PreviousButton,
    NextButton=NextButton,
    PageCounterStyle=PageCounterStyle,
    InitialPage=InitialPage,
    timeout=timeout, ephemeral=ephemeral).start(interaction, pages=embeds)
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
