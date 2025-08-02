<?php
header("Content-Type:application/json");
header("Access-Control-Allow-Headers: *");
header("Access-Control-Allow-Origin: *");
header('Access-Control-Allow-Methods: *');
header("Content-Type:*");
require 'vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;

// $_POST = json_decode(file_get_contents('php://input'), true);
// $file = $_FILES['resume'];

// print_r($file) ;


if (isset($_POST['fullName']) && $_POST['fullName'] != "" && isset($_POST['email']) && $_POST['email'] != "" && isset($_POST['phone']) && $_POST['phone'] != "" && isset($_POST['comments']) && $_POST['comments'] != "") {

    $name           = $_POST['fullName'];
    $email          = $_POST['email'];
    $mobile_no      = $_POST['phone'];
    $comments       = $_POST['comments'];

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format.");
    }

    $domain = substr(strrchr($email, "@"), 1);
    if (!checkdnsrr($domain, 'MX')) {
        die("Invalid domain. No MX records found.");
    }

    $mail2 = new PHPmailer();
    $mail2->isSMTP();
    $mail2->Host = 'mail.nowandforever.com';
    $mail2->SMTPAuth = true;
    $mail2->Username = 'customerservice@nowandforever.com';
    $mail2->Password = 'CS1234***';
    $mail2->SMTPSecure = 'ssl';
    $mail2->Port = 465;

    // Attach the uploaded file
    if (isset($_FILES['resume']) && $_FILES['resume']['error'] === UPLOAD_ERR_OK) {
        $file = $_FILES['resume'];
        $uploadFilePath = $file['tmp_name']; // Temp file location
        $fileName = $file['name'];           // Original file name
        $mail2->addAttachment($uploadFilePath, $fileName); // Full path to temp file and its original name
    }

    // $mail2->setFrom('customerservice@nowandforever.com', 'N&Forever');
    // $mail2->addAddress('carees@nowandforever.com', 'N&Forever');
    $mail2->addAddress('fardeen-intekhaab@mean3.com', 'N&Forever');
    // $mail2->addAddress('umar-jahangir@mean3.com', 'N&Forever');
    // $mail2->addCC('cc1@example.com', 'Elena');
    // $mail2->addBCC('bcc1@example.com', 'Alex');
    $mail2->Subject = "Contact From $email";
    $mail2->isHTML(true);
    $mail2Content = "<!DOCTYPE html>
                <html lang='en'>
                <head>
                <meta charset='UTF-8'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <title>Job Application</title>
                </head>
                <body style='font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; padding: 20px;'>

                <div style='max-width: 600px; margin: 0 auto; background-color: #fff; border-radius: 8px; padding: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>

                    <div style='background-color: #f1f1f1; padding: 15px; border-radius: 5px; margin-top: 20px;'>
                    <p><strong>Full Name:</strong> $name</p>
                    <p><strong>Email:</strong> $email</p>
                    <p><strong>Phone Number:</strong> $mobile_no</p>
                    <p><strong>Comments:</strong></p>
                    <p> $comments</p>
                    </div>

                </body>
                </html>";
    $mail2->Body = $mail2Content;

    if ($mail2->send()) {
        $result = response(200, 'email send sucessfully');
        echo $result;
    } else {
        $result = response(500, 'Mailer Error: ' . $mail2->ErrorInfo);

        echo $result;
    }
} else {
    $result = response(400, 'some fields are required');
    echo $result;
}


function response($status, $response_msg)
{
    $response['Status'] = $status;
    $response['Msg'] = $response_msg;

    $json_response = json_encode($response);
    return $json_response;
}
