import os
import discord
from discord.ext import commands
from e2b_code_interpreter import Sandbox

# Put your actual tokens inside the quotes here:
DISCORD_TOKEN = "MTU2NTc1NzIxOTAyOTY1NTU4Mg.GkhAXF.sWzlDDkRo0rn_VaxXE2mgE1KrE3TEi_VOK9rS8"
os.environ["E2B_API_KEY"] = "e2b_91047eed76e3a92885f8171e7d30a2456121dc48"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("E2B Compiler Bot is ready!")

@bot.command(name="run")
async def run_code(ctx, *, code: str):
    if code.startswith("```"):
        code = code.strip("`")
        if code.startswith("python"):
            code = code[6:].strip()

    await ctx.send(f"⏳ Running code in a secure E2B sandbox for {ctx.author.mention}...")

    try:
        # Use Sandbox.create() instead of Sandbox()
        with Sandbox.create() as sandbox:
            execution = sandbox.run_code(code)

            output_text = ""
            if execution.logs.stdout:
                output_text += "\n".join(execution.logs.stdout)
            if execution.logs.stderr:
                output_text += "\n" + "\n".join(execution.logs.stderr)
            if not output_text and not execution.error:
                output_text = "Code executed successfully with no output."

            if execution.error:
                output_text += f"\nError: {execution.error.name}: {execution.error.value}"

            if len(output_text) > 1900:
                output_text = output_text[:1900] + "\n... (output truncated)"

            embed = discord.Embed(title="💻 E2B Code Execution Result", color=discord.Color.green())
            embed.add_field(name="Output", value=f"```py\n{output_text}\n```", inline=False)
            await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"❌ An error occurred while communicating with E2B: {str(e)}")

bot.run(DISCORD_TOKEN)