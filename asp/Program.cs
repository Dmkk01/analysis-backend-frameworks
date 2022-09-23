using System.Numerics;

var app = WebApplication.Create(args);

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/oops");
}

app.MapGet("/", () => "Health Check");
app.MapGet("/hello", () => {
    Dictionary<string, string> response = new Dictionary<string, string>();
    response["message"] = "Hello World";
    return response;
});

app.MapGet("/fibonacci", () => {
    Dictionary<int, string> numbers = new Dictionary<int, string>();
    BigInteger n1 = new BigInteger(0);
    BigInteger n2 = new BigInteger(1);
    BigInteger nextTerm = new BigInteger(0);

    for (int i = 1; i < 1001; i++)
    {
        nextTerm = n1 + n2;
        n1 = n2;
        n2 = nextTerm;
        numbers[i] = n1.ToString();
    }
    return numbers; 
});

app.MapGet("/oops", () => "Oops! An error happened.");


app.Run();