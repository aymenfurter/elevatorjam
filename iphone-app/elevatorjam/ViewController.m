//
//  ViewController.m
//  elevatorjam
//
//  Created by Aymen Furter on 16.09.22.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}

- (void)updatePreference:(NSString*) songOrGenre {
    NSString *url = @"http://20.203.140.107/user?userId=";
    
    // In the future, this will be the user id of the user.
    url = [url stringByAppendingString:@"7deeea2f-3222-4dfb-82bb-bc445fa1f18f&music="];
    
    // This is the song or genre the user would like to use
    url = [url stringByAppendingString:songOrGenre];
    
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setURL:[NSURL URLWithString:url]];
    [request setHTTPMethod:@"POST"];
    [request setValue:@"application/json" forHTTPHeaderField:@"Accept"];
    
    NSURLResponse *response;
    NSError *err;
    NSData *responseData = [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:&err];

    NSString *str=[[NSString alloc]initWithData:responseData encoding:NSUTF8StringEncoding];
    
    NSString *responseText = @"";
    if ([str isEqualToString:@"\"ok\""]) {
        responseText = @"We've updated your music preference.";
    } else {
        responseText = str;
    }
    
    UIAlertController *alertController = [UIAlertController alertControllerWithTitle:@"Music Preference Updated" message:responseText preferredStyle:UIAlertControllerStyleAlert];
    UIAlertAction* MyAlert = [UIAlertAction actionWithTitle:@"Cool" style:UIAlertActionStyleDefault handler:nil];
    [alertController addAction:MyAlert];
    [self presentViewController:alertController animated:YES completion:nil];
}

- (IBAction)importSong:(id)sender {
    UIAlertController *alertController = [UIAlertController alertControllerWithTitle:@"Song Import" message:@"This feature will come in the next release :)" preferredStyle:UIAlertControllerStyleAlert];
    UIAlertAction* MyAlert = [UIAlertAction actionWithTitle:@"Cool" style:UIAlertActionStyleDefault handler:nil];
    [alertController addAction:MyAlert];
    [self presentViewController:alertController animated:YES completion:nil];

}

- (IBAction)classicalSelected:(id)sender {
    [self updatePreference: @"classical"];
}

- (IBAction)kPopSelected:(id)sender {
    [self updatePreference: @"kpop"];
}

- (IBAction)latinSelected:(id)sender {
    [self updatePreference: @"latin"];
}

- (IBAction)rAndBselected:(id)sender {
    [self updatePreference: @"randb"];
}

- (IBAction)edmSelected:(id)sender {
    [self updatePreference: @"edm"];
}

- (IBAction)hipHopSelected:(id)sender {
    [self updatePreference: @"hiphop"];
}

- (IBAction)popSelected:(id)sender {
    [self updatePreference: @"pop"];
}

- (IBAction)rockSelected:(id)sender {
    [self updatePreference: @"rock"];

}
@end
