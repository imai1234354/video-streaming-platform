# 動画ストリーミングプラットフォーム

このプロジェクトは、AWSサービスを使用して動画のアップロード、エンコード、ストリーミングを行うプラットフォームです。

## 使用技術

- Amazon S3
- Amazon CloudFront
- AWS MediaConvert
- AWS Elemental MediaLive


## セットアップ手順

1. リポジトリをクローンします:
    ```
    git clone <リポジトリURL>
    cd video-streaming-platform
    ```

2. Lambda関数のデプロイ:
    - AWS Lambdaコンソールで新しい関数を作成します。
    - `lambda_function.py`のコードを関数にコピーします。
    - `boto3`ライブラリを含むLambdaレイヤーを作成して関数にアタッチします。

3. S3バケットの作成:
    - S3バケットを作成し、動画ファイルをアップロードします。

4. AWS MediaConvertの設定:
    - AWS MediaConvertのエンドポイントを取得し、`lambda_function.py`のコード内で指定します。
    - メディアコンバートジョブテンプレートを作成し、ジョブ設定をカスタマイズします。

5. CloudFrontの設定:
    - CloudFrontディストリビューションを作成し、S3バケットをオリジンとして設定します。

6. AWS Elemental MediaLiveの設定:
    - ライブストリーミング用のチャネルとエンドポイントを設定します。

## 使用方法

- 動画ファイルをS3バケットにアップロードすると、Lambda関数がトリガーされてAWS MediaConvertで動画がエンコードされます。
- エンコードされた動画はCloudFrontを介してストリーミングされます。
- ライブストリーミングはAWS Elemental MediaLiveを使用して実現します。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。


