package com.example.samsung.communicate;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        GetApi r = new GetApi();

        new Thread(){
            public void run(){
                GetApi r = new GetApi();

                Log.e("Result:",r.getResult().getResult().toString());
            }
        }.start();
    }
}
