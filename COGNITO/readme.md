Install nugets

Amazon.Extensions.CognitoAuthentication

AWSSDK.CognitoIdentity

references:

https://gist.github.com/ccat/b8f46ce380673360e1c52044b7c75bdf
https://csharp.hotexamples.com/examples/Amazon.CognitoIdentity/CognitoAWSCredentials/-/php-cognitoawscredentials-class-examples.html?utm_content=cmp-true

siguietnte paso

        async void OnSignUpButtonClicked(object sender, EventArgs e)
        {
            credentials = new CognitoAWSCredentials(
              "ap-northeast-1:XXXXXXXXXXXXXXXXXXX", // Identity Pool ID
               RegionEndpoint.APNortheast1 // Region
            );

            providerClient = new AmazonCognitoIdentityProviderClient(credentials, RegionEndpoint.APNortheast1);
            SignUpRequest sr = new SignUpRequest();
            sr.ClientId = "XXXXXXXXXX";
            sr.Username = usernameEntry.Text;
            sr.Password = passwordEntry.Text;
            sr.UserAttributes = new List<AttributeType> {
                new AttributeType
                {
                    Name = "email",
                    Value = emailEntry.Text,
                }
            };
            var result = await providerClient.SignUpAsync(sr);
        }

