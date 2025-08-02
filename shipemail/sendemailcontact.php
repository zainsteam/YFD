<?php
header("Content-Type:application/json");
header("Access-Control-Allow-Headers: *");
header("Access-Control-Allow-Origin: *");
header('Access-Control-Allow-Methods: *');
header("Content-Type:*");
require 'vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;

$_POST = json_decode(file_get_contents('php://input'), true);

// print_r($_POST) ;

if (isset($_POST['user_email']) && $_POST['user_email']!="") {
    $name           = $_POST['user_name'];
    $email          = $_POST['user_email'];
    $mobile_no      = $_POST['user_phone'];
    $comments       = $_POST['user_message'];

    $mail = new PHPMailer();
    $mail->isSMTP();
    $mail->Host = 'mail.nowandforever.com';
    $mail->SMTPAuth = true;
    $mail->Username = 'customerservice@nowandforever.com'; 
    $mail->Password = 'CS1234***';
    $mail->SMTPSecure = 'ssl';
    $mail->Port = 465;

    $mail->setFrom('customerservice@nowandforever.com', 'N&Forever');
    $mail->addAddress($email, $name);
    // $mail->addCC('cc1@example.com', 'Elena');
    // $mail->addBCC('bcc1@example.com', 'Alex');
    $mail->Subject = 'Acknowledgement of Your Inquiry';
    $mail->isHTML(true);
    $mailContent = "<p>Thank you for reaching out to us. Your inquiry is important to us, and we appreciate the time you took to contact us. We are currently reviewing your message and will get back to you shortly with a response.</p>";
    $mail->Body = $mailContent;

    if($mail->send()){
        $mail2 = new PHPmailer();
        $mail2->isSMTP();
        $mail2->Host = 'mail.nowandforever.com';
        $mail2->SMTPAuth = true;
        $mail2->Username = 'customerservice@nowandforever.com'; 
        $mail2->Password = 'CS1234***';
        $mail2->SMTPSecure = 'ssl';
        $mail2->Port = 465;

        $mail2->setFrom('customerservice@nowandforever.com', 'N&Forever');
        $mail2->addAddress('hamza-tariq@mean3.com', 'N&Forever');
        // $mail2->addCC('cc1@example.com', 'Elena');
        // $mail2->addBCC('bcc1@example.com', 'Alex');
        $mail2->Subject = "Contact From $email";
        $mail2->isHTML(true);
        $mail2Content = "<p><ul>
                                <li>$name</li>
                                <li>$email</li>
                                <li>$mobile_no</li>
                                <li>$comments</li>
                            </ul>
                        </p>";
        $mail2->Body = $mail2Content;

        if($mail2->send()){
            $result = response( 200,'email send sucessfully');
            echo $result;
        }
        else{
            $result = response( 500,'Mailer Error: ' . $mail2->ErrorInfo);

            echo $result;
        }
    }else{
        $result = response( 500,'Mailer Error: ' . $mail->ErrorInfo);

        echo $result;
    }

}else{
    $result = response( 400,'email field is required');
    echo $result;
}


function response($status,$response_msg){
	$response['Status'] = $status;
	$response['Msg'] = $response_msg;

	$json_response = json_encode($response);
	return $json_response;
}

?>